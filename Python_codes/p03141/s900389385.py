from collections import deque
n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
l.sort(key = lambda x:x[0]+x[1],reverse=True)
ans=0
for i in range(n):
  if i%2==0:
    ans+=l[i][0]
  else:
    ans-=l[i][1]
print(ans)
