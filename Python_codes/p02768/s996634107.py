def main():
    #input data
    import sys
    input = lambda:sys.stdin.readline().strip()
    
    N,A,B = map(int,input().split())
    mod=10**9+7
    #solve
    #二項係数の和=2**n
    #2**n-1-nCa-nCb
    def pow(x, y, mod):
        res = 1
        if y > 0:
            res = pow(x, y // 2, mod)
            if y % 2 == 0:
                res = (res * res) % mod
            else:
                res = (((res * res) % mod) * x) % mod
        return res
        
    def cmb(n, r, mod=10**9+7):
        c = 1
        m = 1
        r = min(n - r, r)
        for i in range(r):
            c = c * (n - i) % mod
            m = m * (i + 1) % mod
        return c * pow(m, mod - 2, mod) % mod
                
    ans = pow(2,N,mod)-1-cmb(N,A,mod)-cmb(N,B,mod)
    print(ans%mod)

if __name__=='__main__':
    main()