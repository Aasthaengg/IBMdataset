import math
n, d = map(int, input().split())
ans = 0
for i in range(n):
    m, p = map(int, input().split())
    if math.sqrt(m ** 2 + p ** 2) <= d:
        ans += 1
print(ans)