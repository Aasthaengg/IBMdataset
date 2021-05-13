def solve(A):
    r = []
    for n in A:
        if n < 2:
            r.append(0)
            continue
        cnt = 0
        while n % 2 == 0:
            n //= 2
            cnt += 1
        r.append(cnt)
    return r


def resolve():
    A = [int(i) for i in input().split()]
    for a in A:
        if a % 2 == 1:
            print(0)
            return
    if min(A) == max(A):
        print(-1)
    else:
        s = solve(A)
        if min(s) == 0 or min(s) != max(s):
            print(min(s))
        else:
            print(min(s) + 1)


resolve()
