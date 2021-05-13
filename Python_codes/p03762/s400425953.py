n, m = map(int, input().split())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))
MOD = int(1e9 + 7)
row = sum([(i+1) * (n-i-1) * (xs[i+1] - xs[i]) % MOD for i in range(n-1)]) % MOD
col = sum([(i+1) * (m-i-1) * (ys[i+1] - ys[i]) % MOD for i in range(m-1)]) % MOD
ans = row * col % MOD
print(ans)