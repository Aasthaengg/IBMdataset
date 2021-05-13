from collections import Counter

n=int(input())
*v,=map(int,input().split())

v0=list(Counter(v[::2]).items())
v1=list(Counter(v[1::2]).items())

v0.sort(key=lambda x:x[1],reverse=True)
v1.sort(key=lambda x:x[1],reverse=True)

k0,ma0=v0[0]
k1,ma1=v1[0]

if k0==k1 and len(v0)==1 and len(v1)==1:
    print(n//2)
elif k0==k1 and len(v0)==1:
    print((n+1)//2-v1[1][1]+n//2-ma0)
elif k0==k1 and len(v1)==1:
    print(n//2-v0[1][1]+(n+1)//2-ma1)
elif k0==k1:
    print(min((n+1)//2-v1[1][1]+n//2-ma0,n//2-v0[1][1]+(n+1)//2-ma1))
else:
    print((n+1)//2-ma0+n//2-ma1)