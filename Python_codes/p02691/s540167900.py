n,*aa = map(int, open(0).read().split())
from collections import Counter
l_cnt = Counter()
r_cnt = Counter()

for i,a in enumerate(aa):
    l_cnt[i+a] += 1

for i,a in enumerate(aa):
    if i-a in l_cnt:
        r_cnt[i-a] += 1

ans = 0
for key in r_cnt:
    ans += l_cnt[key] * r_cnt[key]
print(ans)