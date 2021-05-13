from itertools import accumulate

import sys

input=sys.stdin.readline

N,C=map(int,input().split())
X=[0 for i in range(0,N)]
V=[0 for i in range(0,N)]
for i in range(0,N):
    X[i],V[i]=map(int,input().split())

acu=list(accumulate(V))
if N>=2:
    data=[0 for i in range(0,N)]
    data[N-1]=acu[N-2]-2*X[N-1]
    for i in range(1,N):
        data[N-1-i]=min(data[N-i],acu[N-2-i]-2*X[N-1-i])

    data2=[0 for i in range(0,N)]
    data2[N-1]=acu[N-2]-X[N-1]
    for i in range(1,N):
        data2[N-1-i]=min(data2[N-i],acu[N-2-i]-X[N-1-i])
    ans=[0 for i in range(0,N-1)]
    for i in range(0,N-1):
        ans[i]=min(data[i+1]-acu[i]+X[i]+2*C,data2[i+1]-acu[i]+2*X[i]+C)
    test1=max(acu[i]-X[i] for i in range(0,N))
    k=sum(V)
    test2=max(k-acu[i]-(C-X[i+1]) for i in range(0,N-1))
    test2=max(test2,k-(C-X[0]))
    test3=k-min(ans)
    print(max(0,test1,test2,test3))
else:
    print(max(0,V[0]-min(C-X[0],X[0])))