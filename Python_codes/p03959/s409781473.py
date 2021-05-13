N=int(input())
*T, = map(int,input().split())
*A, = map(int,input().split())

mod = 10**9+7
mT = [T[0]]*N
MT = [T[0]]*N
for i,t in enumerate(T[1:],1):
    if t>T[i-1]:
        mT[i] = t
        MT[i] = t
    else:
        mT[i] = 1
        MT[i] = t
mA = [A[-1]]*N
MA = [A[-1]]*N
for i,a in enumerate(A[-2::-1],2):
    if a>A[-i+1]:
        mA[-i] = a
        MA[-i] = a
    else:
        mA[-i] = 1
        MA[-i] = a
m = [max(a,t) for a,t in zip(mA,mT)]
M = [min(a,t) for a,t in zip(MA,MT)]
ans = 1
for a,b in zip(m,M):
    ans *= max(0,b-a+1)
    ans %= mod
print(ans)