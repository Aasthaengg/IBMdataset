H,W=list(map(int,input().split()))
l=[]
for i in range(H):
   l.append(list(input()))
from collections import Counter
l=sum(l,[])
l=Counter(l)
one=(H%2)*(W%2)
two=(H%2)*(W//2)+(W%2)*(H//2)
four=(H//2)*(W//2)
for i in l.values():
   j=i//4
   i=i%4
   four-=j
   if i==1:
      one-=1
   elif i==2:
      two-=1
   elif i==3:
      one-=1;two-=1
if set([0]) == set([one,two,four]):
   print("Yes")
else:
   if four<0:
      two+=four*2
   four=0
   if set([0]) == set([one,two,four]):
      print("Yes")
   else:
      print("No")