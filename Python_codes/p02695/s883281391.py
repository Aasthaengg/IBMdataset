from itertools import combinations_with_replacement as c_w_r
N,M,Q=map(int,input().split())
s=[list(map(int,input().split()))for _ in range(Q)]
ans=0
for i in c_w_r([i for i in range(1,M+1)],N):
  e=0
  for a,b,c,d in s:
    if i[b-1]-i[a-1]==c:
      e+=d
  ans=max(ans,e)
print(ans)
