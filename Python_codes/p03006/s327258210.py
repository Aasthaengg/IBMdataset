n=int(input())
balls=[]
for i in range(n):
  x,y=map(int,input().split())
  balls.append([x,y])
minans=n
for i in range(0,n-1):
  for j in range(i+1,n):
    p=balls[j][0]-balls[i][0]
    q=balls[j][1]-balls[i][1]
    ballset=set()
    ans=0
    for k in range(n):
      x=balls[k][0]
      y=balls[k][1]
      ballset.add(x*(10**10)+y)
    while ballset:
      current=ballset.pop()
      ballset.add(current)
      y=current%(10**10)
      x=(current-y)//(10**10)
      while (x-p)*(10**10)+(y-q) in ballset:
        x-=p
        y-=q
      while x*(10**10)+y in ballset:
        ballset.remove(x*(10**10)+y)
        x+=p
        y+=q
      ans+=1
    minans=min(minans,ans)
print(minans)