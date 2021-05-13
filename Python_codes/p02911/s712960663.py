N,K,Q=map(int, input().split())
score=[K-Q]*N
for i in range(Q):
  A = int(input())
  score[A-1]+=1
  
for i in range(N):
  if score[i] > 0:
    print('Yes')
    
  else:
    print('No')