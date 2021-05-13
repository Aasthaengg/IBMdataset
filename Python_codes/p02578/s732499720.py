N=int(input())
lis=list(map(int,input().split()))
lis_s=lis.copy()

for i in range(1,N):
  if lis[i]<lis[i-1]:
    lis[i]=lis[i-1]

print(sum(lis)-sum(lis_s))