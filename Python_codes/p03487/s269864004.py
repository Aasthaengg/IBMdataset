N = int(input())
A = list(map(int,input().split()))
from collections import Counter
ctr = Counter(A)

ans = 0
for k,v in ctr.items():
    if v < k:
        ans += v
    else:
        ans += v-k
print(ans)