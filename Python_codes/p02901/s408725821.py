N,M=list(map(int,input().split()))

keys=[[] for _ in range(N)]
dp=[-1]*(2**N)
dp[0]=0

for _ in range(M):
    a,b=list(map(int,input().split()))
    c=list(map(int,input().split()))

    op=2**N-1

    for cc in c:
        op-=2**(cc-1)

    for cc in c:
        keys[cc-1].append((op,a))


def rec(current):
    if dp[current]>-1:
        return dp[current]

    ret=10**10

    i=0
    tmp=current
    while tmp&1==0:
        i+=1
        tmp=tmp>>1
    
    for op,a in keys[i]:
        minc=rec(current&op)
        ret=min(ret,a+minc)
    
    if ret==10**10:
        print(-1)
        exit(0)
    
    dp[current]=ret
    return ret

print(rec(2**N-1))