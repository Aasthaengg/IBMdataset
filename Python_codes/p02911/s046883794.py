N,K,Q=map(int,input().split())
score = [0]*N
for _ in range(Q):
  a = int(input())-1
  score[a]+=1
for s in score:
  if K-Q+s>0:
    print('Yes')
  else:
    print('No')