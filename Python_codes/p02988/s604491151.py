s=0
N=int(input())
L=list(map(int,input().split()))
for i in range(1,N-1):
  if L[i-1]>L[i] and L[i]>L[i+1]:
    s+=1
  if L[i-1]<L[i] and L[i]<L[i+1]:
    s+=1
print(s)