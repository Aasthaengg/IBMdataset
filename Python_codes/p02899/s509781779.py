n=int(input())
a=list(map(int,input().split()))
d=[]
for i in range(1,n+1):
  d.append([a[i-1],i])
d.sort()
ans=[]
for i in range(n):
  ans.append(d[i][1])
  
print(*ans)