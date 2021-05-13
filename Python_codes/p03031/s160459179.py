from itertools import product

N,M=map(int,input().split())
S = []
for i in range(M):
  k,*s = map(int,input().split())
  S.append(s)
P=list(map(int,input().split()))

ans=0
for p in product(range(2),repeat=N):
  cnt1 = 0
  for i in range(M):
    cnt2 = 0
    for j in range(len(S[i])):
      if p[S[i][j]-1]==1:
        cnt2 += 1
    if cnt2 % 2== P[i]:
      cnt1 += 1
  if cnt1 == M:
    ans += 1

print(ans)