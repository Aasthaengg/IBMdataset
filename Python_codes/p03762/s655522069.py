n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
a = [x[i+1] - x[i] for i in range(n-1)]
b = [y[i+1] - y[i] for i in range(m-1)]

MOD = int(1e9+7)
ai = sum([a[i] * (i+1) * max((0, (n-1-i))) % MOD for i in range(n-1)])
bi = sum([b[i] * (i+1) * max((0, (m-1-i))) % MOD for i in range(m-1)])
ans = ai * bi % MOD
print(ans)
