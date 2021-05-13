n=int(input())
v=list(map(int,input().split()))
even=[]
odd=[]
for i in range(n):
  if i%2==0:
    even.append(v[i])
  else:
    odd.append(v[i])
from collections import Counter
even=Counter(even)
odd=Counter(odd)

even=sorted(even.items(),key=lambda x:x[1],reverse=True)
odd=sorted(odd.items(),key=lambda x:x[1],reverse=True)

a=even[0]
if a[1]==n//2:
  b=0
else:
  b=even[1][1]
  
c=odd[0]
if c[1]==n//2:
  d=0
else:
  d=odd[1][1]
  
if a[0]==c[0]:
  print(min(n-a[1]-d,n-b-c[1]))
else:
  print(n-a[1]-c[1])
  
  
  
