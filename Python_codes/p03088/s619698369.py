import sys

sys.setrecursionlimit(10 ** 6)
mod = 10 ** 9 + 7


def is_ok(last4):
    for j in range(4):
        t = list(last4)
        if j != 3:
            t[j], t[j + 1] = t[j + 1], t[j]
        if 'AGC' in ''.join(t):
            return False
    return True


def rec(length, last3):
    if last3 in m[length]:
        return m[length][last3]

    if length == n:
        return 1

    res = 0
    for c in 'ACGT':
        if is_ok(last3 + c):
            res += rec(length + 1, last3[1:] + c)
            res %= mod

    m[length][last3] = res
    return res


n = int(input())
m = [dict() for _ in range(n + 1)]
print(rec(0, 'zzz'))
