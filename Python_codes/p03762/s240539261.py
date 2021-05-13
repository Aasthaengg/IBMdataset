n, m = map(int, input().split( ))
x = list(map(int, input().split( )))
y = list(map(int, input().split( )))

mod = 10**9 +7

W = 0
for i in  range(n-1):
    W += (x[i+1]-x[i]) * (i+1) *(n-i-1)
    W %= mod

H = 0
for i in range(m-1):
    H += (y[i+1]-y[i]) * (i+1) *(m-i-1)
    H %= mod

ans = H * W % mod 

print(ans)