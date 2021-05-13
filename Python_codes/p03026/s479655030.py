import collections
n=int(input())
graph=[]
for i in range(n+1):
  graph.append([])
for i in range(n-1):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
c=list(map(int,input().split()))
c.sort()
c.reverse()
ans=['0']*n
pointer=0
queue=collections.deque([[1,1]])
while queue:
  a=queue.popleft()
  ans[a[0]-1]=str(c[pointer])
  for i in graph[a[0]]:
    if i==a[1]:
      continue
    queue.append([i,a[0]])
  pointer+=1
print(sum(c)-c[0])
print(' '.join(ans))