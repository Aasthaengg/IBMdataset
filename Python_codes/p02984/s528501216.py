N=int(input())
L=list(map(int,input().split()))
a=L[0]
for i in range(N-1):
  a=L[i+1]-a
R=[0]*N
R[0]=a
for i in range(N-1):
  R[i+1]=(L[i]-R[i]//2)*2
print(" ".join(list(map(str,R))))