N=input()
import collections
tmp=list(collections.Counter(N).keys())
ans=float("Inf")
import copy
for i in tmp:
   c=0
   l=copy.deepcopy(N)
   while len(set(l))!=1:
      tmp2=[]
      for j in range(len(l)-1):
         if l[j] ==i or l[j+1]==i:
            tmp2.append(i)
         else:
            tmp2.append(l[j])
      c+=1
      l=copy.deepcopy(tmp2)
   ans=min(ans,c)
print(ans)