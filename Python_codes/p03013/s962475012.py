def getval():
    n,m = map(int,input().split())
    a = [int(input()) for i in range(m)]
    return n,m,a

def main(n,m,a):
    dp = [0 for i in range(n+1)]
    mod = 10**9 + 7
    dp[0] = 1
    it1 = iter(a)
    it2 = iter(a)
    d = dict(zip(it1,it2))
    for i in range(1,n+1):
        if i in d:
            continue
        if i==1:
            dp[1] = dp[0]
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % mod

    print(dp[n])
    #print(dp)

if __name__=="__main__":
    n,m,a = getval()
    main(n,m,a) 