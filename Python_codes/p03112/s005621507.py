A,B,Q=map(int,input().split())
s=[int(input()) for i in range(A)]
t=[int(input()) for i in range(B)]
X=[int(input()) for i in range(Q)]
s.append(2*10**10+1)
t.append(2*10**10+1)
import bisect
for i in range(Q):
  a=bisect.bisect_left(s,X[i])
  b=bisect.bisect_left(t,X[i])
  s1,s2=s[a-1],s[a]
  t1,t2=t[b-1],t[b]
  ans=10**10*2
  for k in [s[a],s[a-1]]:
    for j in [t[b],t[b-1]]:
      d=abs(k-j)+min(abs(k-X[i]),abs(j-X[i]))
      ans=min(ans,d)
  print(ans)