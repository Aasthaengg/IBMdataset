N=int(input())
T,A=map(int,input().split())
W=list(map(int,input().split()))
U=100000000
c=0
for i in range(N):
  W[i]=T-W[i]*0.006
for k in range(N):
  Y=abs(W[k]-A)
  if Y<U:
    U=Y
    c=k
print(c+1)