MOD = 1000000007

n = int(input())
s1 = input()
s2 = input()


def tiles(s1, s2):
    t = []
    c1p, c2p = None, None
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            t.append(1)
        elif c1 != c1p and c2 != c2p:
            t.append(2)
        c1p, c2p = c1, c2
    return t


def solve(s1, s2):
    ncolor = 1
    t = tiles(s1, s2)

    prev = None
    ncolor = 1
    for ti in t:
        if prev is None:
            if ti == 1:
                ncolor *= 3
            if ti == 2:
                ncolor *= 6
        if prev == 1:
            if ti == 1:
                ncolor *= 2
            if ti == 2:
                ncolor *= 2
        if prev == 2:
            if ti == 1:
                ncolor *= 1
            if ti == 2:
                ncolor *= 3
        ncolor %= MOD
        prev = ti

    return ncolor


answer = solve(s1, s2)
print(answer)
