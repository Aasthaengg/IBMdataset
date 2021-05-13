from bisect import*
a,b,q=map(int,input().split())
s=[-10**18]+[int(input()) for _ in range(a)]+[10**18]
t=[-10**18]+[int(input()) for _ in range(b)]+[10**18]
for _ in range(q):
  i=int(input())
  si=bisect_left(s,i)
  ti=bisect_left(t,i)
  print(min(max(s[si],t[ti])-i,i-min(t[ti-1],s[si-1]),
            2*t[ti]-s[si-1]-i,2*s[si]-t[ti-1]-i,
            i+t[ti]-2*s[si-1],i+s[si]-2*t[ti-1]))