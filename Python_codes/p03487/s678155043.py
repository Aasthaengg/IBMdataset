N = int(input())
A = [int(i) for i in input().split()]
from collections import Counter
ans = 0
for k,v in Counter(A).items():
    if v!=k and k>v:
        ans+=v
    elif v!=k and k<v:
        ans+=v-k
print(ans)