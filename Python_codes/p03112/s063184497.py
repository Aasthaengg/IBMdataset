a,b,q=map(int,input().split())
s=[-10**30]+[int(input())for _ in range(a)]+[10**30]
t=[-10**30]+[int(input())for _ in range(b)]+[10**30]
x=[int(input())for _ in range(q)]
from bisect import bisect_left,bisect_right
for xx in x:
  s1=s[bisect_right(s,xx)-1]
  s2=s[bisect_right(s,xx)]
  t1=t[bisect_right(t,xx)-1]
  t2=t[bisect_right(t,xx)]
  ans=[]
  ans.append(abs(s1-t1)+min(abs(xx-s1),abs(xx-t1)))
  ans.append(abs(s1-t2)+min(abs(xx-s1),abs(xx-t2)))
  ans.append(abs(s2-t1)+min(abs(xx-s2),abs(xx-t1)))
  ans.append(abs(s2-t2)+min(abs(xx-s2),abs(xx-t2)))
  print(min(ans))