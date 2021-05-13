from collections import defaultdict
from itertools import accumulate

n,k = map(int, input().split())

a = list(map(int,input().split()))
s = list(accumulate([0]+a))
b = [(s[i]-i)%k for i in range(n+1)]

d = defaultdict(int)
# 初期化
for i in range(min(k-1,n+1)):
    d[b[i]]+=1

ans = 0
for i in range(n):
    # 自分を除外し、k-1個先が存在すれば加える。
    d[b[i]]-=1
    if i+k-1<=n:
        d[b[i+k-1]]+=1
    ans += d[b[i]]

print(ans)


