N=int(input())
A=list(map(int, input().split()))
from collections import Counter
B=Counter(A)
ans=0
for k, v in B.items():
  if int(k)>v:
    ans+=v
  else:
    ans+=v-int(k)
print(ans)