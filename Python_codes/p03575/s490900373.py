import copy
n,m=map(int,input().split())
temp=[[] for i in range(n)]
for i in range(m):
  a,b=map(int,input().split())
  a=a-1
  b=b-1
  temp[a].append(b)
  temp[b].append(a)
count=0
a=[]
c=True
while c:
  c=False
  for i in range(n):
    if len(temp[i])==1 and i not in a:
      temp[temp[i][0]].remove(i)
      a.append(i)
      count=count+1
      c=True
print(count)