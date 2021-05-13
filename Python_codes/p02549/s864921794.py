m = 998244353
def main():
    n,k = map(int,input().split())
    l,r = [],[]
    for _ in range(k):
        l_, r_ = map(int,input().split())
        l.append(l_)
        r.append(r_)

    dp = [0]*(n+1)
    dp[1] = 1
    dpsum = [0]*(n+1)
    dpsum[1] = 1

    for i in range(2,n+1):
        for j in range(k):
            li = i - r[j]
            ri = i - l[j]
            if ri < 0:
                continue
            li = max(li,1)
            dp[i] += dpsum[ri] - dpsum[li-1]
        dpsum[i] = (dpsum[i-1]+dp[i])%m

    print(dp[n]%m)
main()