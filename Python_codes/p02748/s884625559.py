A,B,M=map(int,input().split(" "))
As=list(map(int,input().split(" ")))
Bs=list(map(int,input().split(" ")))
ans=min(As)+min(Bs)
for i in range(M):
  x,y,c=map(int,input().split(" "))
  ans=min(ans,As[x-1]+Bs[y-1]-c)
print(ans)