import bisect
A,B,Q=map(int,input().split())
INF=10**12
S=[-INF]
for i in range(A):
  S.append(int(input()))
S.append(INF)
T=[-INF]
for i in range(B):
  T.append(int(input()))
T.append(INF)
for i in range(Q):
  x=int(input())
  sl=[S[bisect.bisect_left(S,x)],S[bisect.bisect_left(S,x)-1]]
  tl=[T[bisect.bisect_left(T,x)],T[bisect.bisect_left(T,x)-1]]
  ans=[]
  for s in sl:
    for t in tl:
      ans.append(abs(x-s)+abs(s-t))
      ans.append(abs(x-t)+abs(t-s))
  print(min(ans))