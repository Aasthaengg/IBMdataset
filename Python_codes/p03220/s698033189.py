N=int(input())
T,A=map(int,input().split())
H=list(map(int,input().split()))
L=list()
for i in range(N):
  L.append(T-H[i]*0.006)
  L[i]=abs(L[i]-A)
print(L.index(min(L))+1)