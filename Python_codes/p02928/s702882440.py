N, K=map(int, input().split())
a=list(map(int, input().split()))
A=a*2
base=0
matagu=0
for i in range(N):
  for j in range(i+1,2*N):
    if A[i]>A[j]:
      if j>=N:
        matagu+=1
      else:
        base+=1
baserep=K
matagurep=K*(K-1)//2
waru=10**9+7
ans=(base*baserep+matagu*matagurep)%waru
print(ans)