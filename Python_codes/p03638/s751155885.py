H,W=map(int,input().split())
N=int(input())
A=list(map(int,input().split()))

ans=[[0]*W for _ in range(H)]
x=0
y=0
dir=1
for a in range(1,N+1):
  for _ in range(A[a-1]):
    ans[y][x]=a
    if dir==1 and x==W-1:
      y+=1
      dir=-1
    elif dir==1:
      x+=1
    elif dir==-1 and x==0:
      y+=1
      dir=1
    elif dir==-1:
      x-=1
      
for i in ans:
  print(*i)