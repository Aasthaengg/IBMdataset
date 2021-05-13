import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n

n, *a = map(int, read().split())

res = gcd(a[0],a[1])
for i in range(2,n):
    res = gcd(res, a[i])

print(res)