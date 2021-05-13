import itertools 
n,m=map(int,input().split());l1=[];l2=[];ans=0
while len(l1)<n:
  if len(l1)==0:
    l1.append(2)
  else:
    l1.append(l1[-1]+2)
while len(l2)<m:
  if len(l2)==0:
    l2.append(1)
  else:
    l2.append(l2[-1]+2)
for i in list(itertools.combinations(l1+l2, 2)):
  if sum(i)%2==0:
    ans+=1
print(ans)