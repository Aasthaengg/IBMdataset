N=int(input())
L=list(map(int,input().split()))
for i in range(N):
  L[i]=1/L[i]
print(1/sum(L))