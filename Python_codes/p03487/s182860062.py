n, *aa = map(int, open(0).read().split())

from collections import Counter

ans = 0

for k, count in Counter(aa).items():
    if count<k:
        ans += count
    else:
        ans += count-k

print(ans)