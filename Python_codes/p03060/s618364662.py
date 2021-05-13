N=int(input())
V=list(map(int,input().split()))
C=list(map(int,input().split()))
real=[]
for i in range(0,N):
  tmp=V[i]-C[i]
  real.append(tmp)
#print(real)
sum=0
for i in range(0,N):
  if real[i]>0:
    sum+=real[i]
print(sum)