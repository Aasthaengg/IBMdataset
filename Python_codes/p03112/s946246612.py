import sys
input=sys.stdin.readline
a,b,q=map(int,input().split())
s=[-10**11]
t=[-10**11]
for i in range(a):
	s.append(int(input()))
s.append(10**11)
for i in range(b):
	t.append(int(input()))
t.append(10**11)
import bisect
for i in range(q):
	x=int(input())
	s_l=bisect.bisect_left(s,x)
	t_l=bisect.bisect_left(t,x)
	ans1=x-min(s[s_l-1],t[t_l-1])
	ans2=max(s[s_l],t[t_l])-x
	ans3=min(s[s_l]-x,x-t[t_l-1])+s[s_l]-t[t_l-1]
	ans4=min(t[t_l]-x,x-s[s_l-1])+t[t_l]-s[s_l-1]
	print(min(ans1,ans2,ans3,ans4))