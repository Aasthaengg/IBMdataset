n, m = map(int, input().split())
a = list(map(int, input().split()))

cum =[0 for _ in range(n)]
cum[0] = a[0] % m
for i in range(1, n):
    cum[i] = cum[i-1] + a[i] % m
    cum[i] %= m

from collections import Counter
c = Counter(cum)

ans = sum((v*(v-1)//2) for v in c.values())
if 0 in c:
    ans += c[0]
print(ans)
