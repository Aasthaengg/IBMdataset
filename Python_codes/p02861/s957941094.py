#C
N=int(input())
XY=[list(map(int,input().split())) for i in range(N)]
fact=[1 for i in range(N+1)]
for i in range(1,N+1):
  fact[i]=fact[i-1]*i

ans=0
for i in range(N):
  for j in range(i+1,N):
    x0,y0=XY[i]
    x1,y1=XY[j]
    dis=pow((x0-x1)**2+(y0-y1)**2,0.5)
    ans+=dis*fact[N-1]*2

print(ans/fact[N])