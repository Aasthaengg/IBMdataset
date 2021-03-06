def main():
    #input data
    import sys
    input = lambda:sys.stdin.readline().strip()
    
    N,A,B = map(int,input().split())
    mod=10**9+7
    #solve
    #二項係数の和=2**n
    #2**n-1-nCa-nCb
    def cmb(n, r, mod=10**9+7):
        r = min(r, n-r)
        res = 1
        for i in range(r):
            res = res * (n - i) * pow(i+1, mod-2, mod) % mod
        return res
                
    ans = pow(2,N,mod)-1-cmb(N,A,mod)-cmb(N,B,mod)
    print(ans%mod)

if __name__=='__main__':
    main()