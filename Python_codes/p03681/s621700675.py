# https://atcoder.jp/contests/abc065/tasks/arc076_a

n, m = [int(i) for i in input().split()]


def perm(x):
    a = 1
    for i in range(1, x + 1):
        a = (a * i) % (10**9 + 7)
    return a


if abs(m - n) > 1:
    print(0)
    quit()


if m == n:
    ans = (2 * perm(m) * perm(n)) % (10**9 + 7)
else:
    ans = (perm(m) * perm(n)) % (10**9 + 7)

print(ans)
