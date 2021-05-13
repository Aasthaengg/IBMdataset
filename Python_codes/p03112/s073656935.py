import bisect
a,b,q=map(int,input().split())
INF=10**18
s=[-INF]+[int(input()) for _ in range(a)]+[INF]
t=[-INF]+[int(input()) for _ in range(b)]+[INF]

for k in range(q):
  x=int(input())
  i=bisect.bisect_right(s,x)
  j=bisect.bisect_right(t,x)
  d=INF
  for S in [s[i-1],s[i]]:
    for T in [t[j-1],t[j]]:
      d1=abs(S-x)+abs(S-T)
      d2=abs(T-x)+abs(S-T)
      d=min(d,d1,d2)
  print(d)

