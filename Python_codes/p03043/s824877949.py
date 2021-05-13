from math import ceil, log2
n, k = map(int, input().split())
p = 1 / n
res = max(0, p*(n-k+1))
for i in range(1, min(n+1, k)):
    res += p*(0.5**ceil(log2(k/i)))
print(res)