import bisect
a,b,q=map(int,input().split())
A=[-1*(10**12)]
B=[-1*(10**12)]
for i in range(a):
    A.append(int(input()))
for i in range(b):
    B.append(int(input()))

A.append(10**12)
B.append(10**12)

for i in range(q):
    x=int(input())
    ia=bisect.bisect_right(A,x)

    ms=A[ia-1]
    ps=A[ia]
    
    ib=bisect.bisect_right(B,x)
    
    mt=B[ib-1]
    pt=B[ib]
        
    ans=min(x-min(ms,mt),max(ps,pt)-x,(ps-mt)+min(ps-x,x-mt),(pt-ms)+min(pt-x,x-ms))
    print(ans)