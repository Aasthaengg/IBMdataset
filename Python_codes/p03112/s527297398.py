import bisect

INF=10**18
A,B,Q=map(int,input().split())
S=[0]*(A+2)
T=[0]*(B+2)
S[0],T[0]=-INF,-INF
S[A+1],T[B+1]=INF,INF

for i in range(1,A+1):
    S[i]=int(input())

for i in range(1,B+1):
    T[i]=int(input())

for i in range(Q):
    x=int(input())
    b,d=bisect.bisect_right(S,x), bisect.bisect_right(T,x)
    ans=INF
    for s in [S[b-1],S[b]]:
        for t in [T[d-1],T[d]]:
            d1,d2=abs(s-x)+abs(t-s),abs(t-x)+abs(s-t)
            ans=min(ans,d1,d2)
    print(ans)