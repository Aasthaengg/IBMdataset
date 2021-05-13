N=int(input())

T = list(map(int,input().split()))
A = list(map(int,input().split()))

count=0
for i in range(N):
    if A[i]==T[N-1] and T[i]==T[N-1]:
        count+=1


if count==0:
    print(0)
else:
    count=max(0,count-2)

    mod = 10**9+7
    d = pow(T[N-1],count,mod)

    from collections import Counter

    tc=Counter(T)

    for key in tc.keys():
        if key!=T[N-1]:
            d*=pow(key,tc[key]-1,mod)
            d%=mod

    ac=Counter(A)

    for key in ac.keys():
        if key!=T[N-1]:
            d*=pow(key,ac[key]-1,mod)
            d%=mod

    print(d)