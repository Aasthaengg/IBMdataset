n,m=map(int,input().split())
h=list(map(int,input().split()))
x=[[] for _ in range(n+1)]
for i in range(m):
  a,b=map(int,input().split())
  x[a].append(h[b-1])
  x[b].append(h[a-1])
count=0
for j in range(1,n+1):
  if x[j]==[]:
    count+=1
  else:
    if h[j-1]>max(x[j]):
      count+=1
print(count)