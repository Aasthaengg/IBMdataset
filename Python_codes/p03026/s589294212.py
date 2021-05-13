from collections import deque
n=int(input())
ans=[0 for i in range(n)]
l=[[] for i in range(n+1)]
for i in range(n-1):
  a,b=map(int,input().split())
  l[a].append(b)
  l[b].append(a)
l1=sorted(list(map(int,input().split())))
l1=l1[::-1]
sum=0
for i in range(1,n):
  sum+=l1[i]
q=deque(l1)
q1=deque([[1]])
while q:
  l2=q1.popleft()
  for i in l2:
    if ans[i-1]!=0:
      pass
    else:
      n2=q.popleft()
      ans[i-1]=n2
      q1.append(l[i])
print(sum)
answ=""
for i in range(n):
  answ+=str(ans[i])+" "
print(answ)