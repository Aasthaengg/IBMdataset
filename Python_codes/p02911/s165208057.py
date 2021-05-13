N,K,Q=list(map(int, input().split()))
L=[0]*N
for _ in range(Q):
  i=int(input())
  L[i-1]+=1
for i in range(N):
  if L[i]>Q-K:
    print('Yes')
  else:
    print('No')