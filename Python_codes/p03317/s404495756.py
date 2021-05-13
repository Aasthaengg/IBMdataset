def waru(a,b):
  if a%b==0:
    return a//b
  else:
    return (a//b)+1
N,K=map(int,input().split())
L=list(map(int,input().split()))
mina=min(L)
ind=list()
R=[0]*N
for i in range(N):
  if L[i]==mina:
    ind.append(i)
    R[i]+=1
for i in range(1,N):
  R[i]=R[i-1]+R[i]
s=ind[0]
a=waru(s,K-1)
b=(a*(K-1))-s
susumi=b+s+1
#.......a. b+sだけ進んでる
while True:
  if susumi>=N:
    print(a)
    break
  if R[min(susumi+K,N-1)]-R[susumi]>0:
    susumi+=K
    a+=1
  else:
    susumi+=K-1
    a+=1