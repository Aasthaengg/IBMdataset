import sys
input = sys.stdin.buffer.readline
from collections import defaultdict
import copy

def main():
    N,M = map(int,input().split())
    d = defaultdict(int)
    MOD = 10**9+7
    R = 10**5+100
    fac = [0 for _ in range(R+1)]
    fac[0],fac[1] = 1,1
    inv = copy.deepcopy(fac)
    invfac = copy.deepcopy(fac)
    
    for i in range(2,R+1):
        fac[i] = (fac[i-1]*i)%MOD
        inv[i] = MOD-(MOD//i)*inv[MOD%i]%MOD
        invfac[i] = (invfac[i-1]*inv[i])%MOD
        
    def coef(x,y):
        num = (((fac[x+y]*invfac[y])%MOD)*invfac[x]%MOD)
        return num

    while M%2 == 0:
        d[2] += 1
        M //= 2
    f = 3
    while f ** 2 <= M:
        if M % f == 0:
            d[f] += 1
            M //= f
        else:
            f += 2
    if M != 1:
        d[M] += 1
    
    l = list(d.values())
    ans = 1
    for num in l:
        ans *= coef(num,N-1)
        ans %= MOD
        
    print(ans)
    
if __name__ == "__main__":
    main()