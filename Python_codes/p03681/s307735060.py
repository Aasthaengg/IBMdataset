import sys

sys.setrecursionlimit(1000000)

mod = 1000000007


def fac(n):
    v = 1
    for i in range(n):
        v = int(((i+1) * v) % mod)
    return v


n, m = map(int, input().split())
if abs(m-n) > 1:
    print(0)
    exit()
n = int(fac(n) % (mod))
m = int(fac(m) % (mod))
ans = int((n*m) % (mod))
if abs(n-m) == 0:
    ans = int((ans*2) % mod)
print(ans)
