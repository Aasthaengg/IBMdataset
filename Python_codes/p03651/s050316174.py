import sys
input = lambda: sys.stdin.readline().rstrip()


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n, k = map(int, input().split())
a = list(map(int, input().split()))
g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])
if k % g == 0 and max(a) >= k:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
