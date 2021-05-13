from bisect import bisect_left

A,B,Q=list(map(int,input().split()))
s=[-10**11]+[int(input()) for _ in range(A)]+[10**11]
t=[-10**11]+[int(input()) for _ in range(B)]+[10**11]
x=[int(input()) for _ in range(Q)]


for xi in x:
    p1=bisect_left(s,xi)
    p2=bisect_left(t,xi)
    l=10**11
    for ss in s[p1-1:p1+1]:
        for tt in t[p2-1:p2+1]:
            l=min(l,min(abs(ss-xi),abs(tt-xi))+abs(ss-tt))
    
    print(l)
