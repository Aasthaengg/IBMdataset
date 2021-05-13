import sys
input = sys.stdin.readline

mod = 10**9+7
n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
f = 0
for j in range(m-1):
    f = (f + (y[j+1]-y[j])*(j+1)*(m-j-1)) % mod
ans = 0
for i in range(n-1):
    ans = (ans + (x[i+1]-x[i])*(i+1)*(n-i-1)*f) % mod
print(ans)