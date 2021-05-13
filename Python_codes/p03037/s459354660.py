N,M = map(int,input().split())
L = []
R = []
 
for m in range(M):
  l,r = map(int,input().split())
  L+=[l]
  R+=[r]
 
print(max(0,min(R)-max(L)+1))