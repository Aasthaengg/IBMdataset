N = int(input())
l=[]
if N==1:
   print(1)
   exit()
for i in range(N):
   a,b=map(int,input().split())
   l.append((a,b))
l2=[]
for i in range(N):
   for j in range(N):
      if i!=j:
         l2.append((l[i][0]-l[j][0],l[i][1]-l[j][1]))
from collections import Counter
l2=max(Counter(l2).values())
print(N-l2)