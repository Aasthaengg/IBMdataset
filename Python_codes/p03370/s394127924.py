N,X=map(int,input().split())
m=[0]*N
count=0
for i in range(N):
  m[i]=int(input())
  X-=m[i]
  count+=1
count+=X//min(m)
print(count)