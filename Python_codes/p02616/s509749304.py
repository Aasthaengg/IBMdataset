import sys

# after これ通る？コピペs


def solve(n, k, aaa):
    MOD = 10 ** 9 + 7

    if n == k:
        ans = 1
        for a in aaa:
            ans = ans * a % MOD
        return ans

    pos = []  # Strictly, Non-neg
    neg = []
    for a in aaa:
        if a >= 0:
            pos.append(a)
        elif a < 0:
            neg.append(a)

    if len(pos) == 0:
        if k % 2 == 1:
            neg.sort(reverse=True)
        else:
            neg.sort()
        ans = 1
        for a in neg[:k]:
            ans = ans * a % MOD
        return ans

    pos.sort()
    neg.sort(reverse=True)
    ans = 1
    r = k

    if r % 2 == 1:
        ans = ans * pos.pop() % MOD
        r -= 1

    while r > 0:
        if len(pos) <= 1:
            ans = ans * neg.pop() * neg.pop() % MOD
        elif len(neg) <= 1:
            ans = ans * pos.pop() * pos.pop() % MOD
        else:
            pm = pos[-1] * pos[-2]
            nm = neg[-1] * neg[-2]
            if pm > nm:
                ans = ans * pos.pop() * pos.pop() % MOD
            else:
                ans = ans * neg.pop() * neg.pop() % MOD
        r -= 2

    return ans


n, k, *aaa = map(int, sys.stdin.buffer.read().split())
print(solve(n, k, aaa))
