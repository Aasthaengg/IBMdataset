n, m = map(int, input().split())
a = list(map(int, input().split()))
from collections import Counter
c = Counter()
sum_val = 0
c[sum_val] += 1
for i in range(n):
    sum_val += a[i]
    sum_val %= m
    c[sum_val] += 1
ans = 0
for v in c.values():
    ans += v*(v-1)//2
print(ans)


