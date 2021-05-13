n, m = map(int, input().split())
a_lis = list(map(int, input().split()))
asum_mods = [0]
tmp_sum = 0
for i in range(n):
    tmp_sum += a_lis[i]
    asum_mods.append(tmp_sum % m)
import collections
c = collections.Counter(asum_mods).values()
ans = 0
for b in c:
    ans += b * (b - 1) // 2
print(ans)