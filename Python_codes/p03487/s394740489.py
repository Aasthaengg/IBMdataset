from collections import Counter
N=int(input())
L=list(map(int,input().split()))
ke=list(Counter(L).values())
val=list(Counter(L).keys())
ans=0
for i in range(len(val)):
  if val[i]>ke[i]:
    ans+=ke[i]
  else:
    ans+=ke[i]-val[i]
print(ans)