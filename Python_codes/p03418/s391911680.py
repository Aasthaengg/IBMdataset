n, k = map(int, input().split())

res = 0
for i in range(k+1, n+1):
    res += (i - k) * (n // i) + max(0, n % i - k + 1)
if k == 0:
    res -= n

print(res)