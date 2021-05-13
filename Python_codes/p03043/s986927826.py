import math


n, k = map(int, input().split())

ans = max(0, (n-k+1)/n)
for i in range(1, n+1):
    if i >= k:
        break
    x = math.ceil(math.log2(k/i))
    ans += (1/n) * (1/2)**x
print(ans)
