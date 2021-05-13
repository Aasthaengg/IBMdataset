from collections import defaultdict
d=defaultdict(int)

A=input()
for i in A:
  d[i]+=1
  
li=list(d.values())
li2=[i*(i-1)//2 for i in li]

n=len(A)

print(n*(n-1)//2+1-sum(li2))