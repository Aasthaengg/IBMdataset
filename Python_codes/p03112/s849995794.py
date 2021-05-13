a,b,q=map(int,input().split())
s=[int(input()) for i in range(a)]
t=[int(input()) for i in range(b)]
x=[int(input()) for i in range(q)]

from bisect import bisect

for i in range(q):
    y=bisect(s,x[i])
    z=bisect(t,x[i])
    k=([0] if y==0 else [a-1] if y==a else [y-1,y])
    l=([0] if z==0 else [b-1] if z==b else [z-1,z])
    mi=100000000000000
    for n in k:
        for m in l:
            if abs(s[n]-x[i])>abs(t[m]-x[i]):
                sub1,sub2=t[m],s[n]
            else:
                sub1,sub2=s[n],t[m]
            mi=min(mi,abs(sub1-x[i])+abs(sub2-sub1))
    print(mi)