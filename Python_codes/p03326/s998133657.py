N,M=map(int,input().split())
XYZ=[list(map(int,input().split())) for _ in range(N)]

ans=0

for i in range(2**3):
  L=[]
  tmp=0
  for j in range(N):
    L.append((XYZ[j][0] if i%2==0 else -XYZ[j][0])
              +(XYZ[j][1] if (i>>1)%2==0 else -XYZ[j][1])
              +(XYZ[j][2] if (i>>2)%2==0 else -XYZ[j][2]))
    L.sort(reverse=True)
    tmp=sum(L[:M])
  ans=max(ans,tmp)
  
print(ans)