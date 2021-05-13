import bisect,sys
input = sys.stdin.readline
a,b,q = map(int,input().split())
inf = 10**18
s = [-inf]+[int(input()) for i in range(a)]+[inf]
t = [-inf]+[int(input()) for i in range(b)]+[inf]
for i in range(q):
  x = int(input())
  i = bisect.bisect_right(s,x)
  j = bisect.bisect_right(t,x)
  print(min(max(s[i],t[j])-x,x-min(s[i-1],t[j-1]),min(s[i]-x,x-t[j-1])+s[i]-t[j-1],min(t[j]-x,x-s[i-1])+t[j]-s[i-1]))