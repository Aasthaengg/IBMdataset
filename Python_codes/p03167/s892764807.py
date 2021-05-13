def getval():
    h,w = map(int,input().split())
    a = [input() for i in range(h)]
    return h,w,a 

def main(h,w,a):
    mod = 10**9 + 7
    dp = [[0 for i in range(w+1)] for i in range(h+1)]
    dp[1][1] = 1
    for i in range(1,h+1):
        for j in range(1,w+1):
            if i==1 and j==1:
                continue
            if a[i-1][j-1]=="#":
                continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
    print(dp[h][w])

if __name__=="__main__":
    h,w,a = getval()
    main(h,w,a) 
