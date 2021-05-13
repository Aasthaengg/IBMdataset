import collections
n,x,y=map(int,input().split())
lst=[]
num=[0]*(n+1)
for i in range(1,n):
  for j in range(i+1,n+1):
    k=min(abs(i-j),abs(i-x)+1+abs(j-y),abs(i-y)+1+abs(j-x))
    if num[k]==0:
      num[k]+=1
    lst.append(k)
    
Lst=list(collections.Counter(lst).items())
key=0
for i in range(1,n):
  if num[i]==0:
    print(0)
  else:
    print(Lst[key][1])
    key+=1