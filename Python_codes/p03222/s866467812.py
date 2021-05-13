h,w,K = map(int,input().split())

mod = 10**9+7

num = 2**(w-1)

li = []

if w == 1:
    if K == 1:
        print(1)
        exit()
    else:
        print(0)
        exit()

for i in range(num):
    tmp = format(i, '0'+str(w-1)+'b')
    cnt = 0
    for j in range(w-1):
        if tmp[j] == '1':
            if cnt == 1:
                break
            else:
                cnt = 1
        else:
            cnt = 0
        if j == w-2:
            li.append(tmp)
    #print(tmp)

dp = [[0 for i in range(w)] for j in range(h+1)]

dp[0][0] = 1

for i in range(h):
    #print(i)
    for j in range(len(li)):
        for k in range(w):
            #print(li[j],li[j][0] == '1')
            if k == 0:
                if li[j][k] == '1':
                    dp[i+1][k+1] += dp[i][k]
                    dp[i+1][k+1] %= mod
                else:
                    dp[i+1][k] += dp[i][k]
                    dp[i+1][k] %= mod
            elif k == w-1:
                if li[j][k-1] == '1':
                    dp[i+1][k-1] += dp[i][k]
                    dp[i+1][k-1] %= mod
                else:
                    dp[i+1][k] += dp[i][k]
                    dp[i+1][k] %= mod
            else:
                if li[j][k-1] == '1':
                    dp[i+1][k-1] += dp[i][k]
                    dp[i+1][k-1] %= mod
                elif li[j][k] == '1':
                    #print(dp[i][k],i,k,i+1,k+1)
                    dp[i+1][k+1] += dp[i][k]
                    #print(dp[i+1][k+1],dp)
                    dp[i+1][k+1] %= mod
                else:
                    dp[i+1][k] += dp[i][k]
                    dp[i+1][k] %= mod
                    
print(dp[h][K-1])