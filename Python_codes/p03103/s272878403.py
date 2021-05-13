n,m=map(int,input().split())
costs=[]
for i in range(n):
  a,b=map(int,input().split())
  costs.append([a,b])
costs=sorted(costs, key=lambda student: student[0])
pointer=0
ans=0
while m>0:
  costs[pointer][1]-=1
  ans+=costs[pointer][0]
  m-=1
  if costs[pointer][1]==0:
    pointer+=1
print(ans)