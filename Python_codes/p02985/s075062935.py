import sys
input = sys.stdin.buffer.readline
import copy
from collections import deque

def main():
    N,K = map(int,input().split())
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
        
    go = [False for _ in range(N)]
    go[0] = True
    for num in edge[0]:
        go[num] = True
    MOD = 10**9+7
    fac = [0 for _ in range(K+1)]
    fac[0],fac[1] = 1,1
    inv = copy.deepcopy(fac)
    invfac = copy.deepcopy(fac)
    
    for i in range(2,K+1):
        fac[i] = (fac[i-1]*i)%MOD
        inv[i] = MOD-(MOD//i)*inv[MOD%i]%MOD
        invfac[i] = (invfac[i-1]*inv[i])%MOD
        
    def per(x,y):
        num = ((fac[x]*invfac[x-y])%MOD)
        return num

    if K-1 < len(edge[0]):
        print(0)
        exit()
    ans = K*(per(K-1,len(edge[0])))

    q = deque(edge[0])
    while q:
        now = q.popleft()
        use = 0
        for fol in edge[now]:
            if not go[fol]:
                use += 1
                go[fol] = True
                q.append(fol)
        if use > K-2:
            print(0)
            exit()
        num = per(K-2,use)
        ans *= num
        ans %= MOD
        
    print(ans%MOD)

if __name__ == "__main__":
    main()