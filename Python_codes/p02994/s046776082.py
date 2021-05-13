N,L=map(int,input().split())
score = [L+i for i in range(N)]
SUM=sum(score)

MIN=10**9
argmin=-1
for i in range(N):
  res = abs(SUM - (SUM-score[i]))
  if res < MIN:
    MIN = res
    argmin=i

print(SUM-score[argmin])