import sys
input = sys.stdin.buffer.readline

def main():
    N,K = map(int,input().split())
    MOD = 10**9+7
    
    fac = [0]*(N+1)
    invfac = [0]*(N+1)
    fac[0],fac[1] = 1,1
    invfac[0],invfac[1] = 1,1
    
    for i in range(2,N+1):
        fac[i] = (fac[i-1]*i)%MOD
        
    invfac[-1] = pow(fac[-1],MOD-2,MOD)
    for i in range(N,0,-1):
        invfac[i-1] = (invfac[i]*i)%MOD
        
    def comb(x,y):
        return (fac[x]*invfac[y]*invfac[x-y])%MOD
        
    ans = 0
    for i in range(min(N,K+1)):
        a = comb(N,i)
        b = comb(N-1,N-i-1)
        ans += (a*b)%MOD
        
    print(ans%MOD)

if __name__ == "__main__":
    main()
