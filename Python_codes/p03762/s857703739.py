
n, m = map(int,input().split())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))

XX = [X[i+1]-X[i] for i in range(n-1)]
YY = [Y[i+1]-Y[i] for i in range(m-1)]

mod = 10**9 + 7

ans = 0
ans0 = 0
for i in range(1, n):
    ans1 = (i * (n-i)) % mod
    ans1 = (ans1 * XX[i-1]) % mod
    ans0 = (ans0 + ans1) % mod

for i in range(1, m):
    ans1 = (i * (m-i)) % mod
    ans1 = (ans1 * YY[i-1]) % mod
    ans1 = (ans1 * ans0) % mod
    ans = (ans + ans1) % mod

print(ans)
