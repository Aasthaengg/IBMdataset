N,M=map(int,input().split())
AB=[]
for i in range(N):
  a,b=map(int,input().split())
  AB.append([a,b])
AB.sort()
ans=0
count=0
while(count<N):
  if AB[count][1]<=M:
    ans+=AB[count][0]*AB[count][1]
    M-=AB[count][1]
    count+=1
  else:
    ans+=AB[count][0]*M
    break
print(ans)