from bisect import bisect

a,b,q=map(int,input().split())
s=[-10**18]+[int(input()) for i in range(a)]+[10**18]
t=[-10**18]+[int(input()) for i in range(b)]+[10**18]

for i in range(q):
  x=int(input())
  s_inx=bisect(s,x)
  t_inx=bisect(t,x)

  s_l=s[s_inx-1]
  s_r=s[s_inx]

  t_l=t[t_inx-1]
  t_r=t[t_inx]

  ans=10**18
  for i in [s_l,s_r]:
    for j in [t_l,t_r]:
      ans=min(ans,abs(i-x)+abs(j-i))

  for i in [t_l,t_r]:
    for j in [s_l,s_r]:
      ans=min(ans,abs(i-x)+abs(j-i))

  print(ans)