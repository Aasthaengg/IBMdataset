n=int(input())
old=[0,0,0]
for i in range(n):
  t,x,y=map(int,input().split())
  tt=t-old[0]
  xx=x-old[1]
  yy=y-old[2]
  dist=abs(xx)+abs(yy)
  if tt%2 != (xx+yy)%2 or dist>tt:
    print("No")
    exit()
  old=[t,x,y]
  
print("Yes")