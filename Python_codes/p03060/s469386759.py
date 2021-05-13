N=int(input())
V=list(map(int,input().split()))
C=list(map(int,input().split()))
netV = [V[i] - C[i] for i in range(N)]

netV=sorted(netV,reverse=True)

SUM=0
for i in range(N):
  if netV[i]>0:
    SUM += netV[i]
  else:
    break

print(SUM)