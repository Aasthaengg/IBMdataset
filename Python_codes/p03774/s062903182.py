N,M=map(int,input().split())
A=[tuple(map(int,input().split())) for _ in range(N)]
B=[tuple(map(int,input().split())) for _ in range(M)]

for i in range(N):
  x,y=A[i]
  temp=10**9
  ans=1
  for j in range(M):
    X,Y=B[j]
    manhattan=abs(x-X)+abs(y-Y)
    if temp>manhattan:
      temp=min(temp,manhattan)
      ans=j+1
  else:
    print(ans)