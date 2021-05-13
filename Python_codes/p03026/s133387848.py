from collections import deque
n=int(input())
l=[list(map(int,input().split())) for i in range(n-1)]
c=list(map(int,input().split()))
c.sort()
connection=[[] for i in range(n)]
ans=[0 for i in range(n)]
for i in range(n-1):
  connection[l[i][0]-1].append(l[i][1]-1)
  connection[l[i][1]-1].append(l[i][0]-1)
next=[0]
next=deque(next)
check=[-1 for i in range(n)]
check[0]=1
ct=n
while ct>0:
  ct-=1
  x=next.popleft()
  ans[x]=str(c[ct])
  for i in range(len(connection[x])):
    if check[connection[x][i]]==-1:
      next.append(connection[x][i])
      check[connection[x][i]]=1
print(sum(c)-c[n-1])
print(' '.join(ans))