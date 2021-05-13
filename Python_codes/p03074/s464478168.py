n,k=map(int,input().split())
s=input()
l=[]
if s[0]=="0":
  l.append(0)

from itertools import groupby,accumulate
gr=groupby(s)

for K,g in gr:
  l.append(len(list(g)))

l_sum=list(accumulate(l))
l_sum=[0]+l_sum

add=2*k+1
ans=0
for i in range(0,len(l)+1,2):
  left=i
  right=min(i+add,len(l))
  tmp=l_sum[right]-l_sum[left]
  ans=max(tmp,ans)
print(ans)