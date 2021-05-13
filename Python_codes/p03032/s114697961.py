import random

N,K=map(int,input().split())
V=list(map(int,input().split()))

if K==0:
    print(0)
    exit()

if 0:
    V=[random.randint(-10**7,10**7) for i in range(N)]

ans=-float("inf")

for i in range(N+1):
    for j in range(N-i+1):
        if i+j>K:
            continue
        tmp=[V[k] for k in range(i)]
        for k in range(j):
            tmp.append(V[-1-k])
        tmp.sort()
        rest=K-i-j
        minus=0
        base=sum(tmp)
        for k in range(min(rest,len(tmp))):
            if tmp[k]<0:
                minus+=tmp[k]
            else:
                break
        test=base-minus
        ans=max(ans,test)

print(ans)
