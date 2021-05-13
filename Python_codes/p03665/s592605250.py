def main():
    n,p = map(int,input().split())
    a = list(map(int,input().split()))
    D = {0:0, 1:0}
    for i in range(n):
        D[a[i]%2]+=1
    ans = 0

    nCr = {}
    def cmb(n, r):
        if r == 0 or r == n: return 1
        if r == 1: return n
        if (n,r) in nCr: return nCr[(n,r)]
        nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
        return nCr[(n,r)]
    if p==0:
        for i in range(D[1]//2+1):
            ans += cmb(D[1],2*i)
    else:
        for i in range(D[1]//2):
            ans += cmb(D[1],2*i+1)
    print(ans * pow(2,D[0]))

if __name__ == "__main__":
    main()
