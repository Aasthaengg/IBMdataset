import sys

def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

ans = gcd(a[0], a[1])
for x in a[2:]:
    tmp = gcd(ans, x)
    if tmp < ans:
        ans = tmp
print(ans)
