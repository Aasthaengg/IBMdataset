def main():
    import itertools
    mod = 10**9+7
    H,W,K = map(int, input().split())
    zero = [0,1]
    dp = [[[0]*W for i in range(W)] for j in range(H+1)]
    for i in range(W):
        dp[0][i][i] = 1
    #print(dp)
    for h in range(1,H+1):
        
        for v in itertools.product(zero, repeat = W-1):
            flag = 0
            for i in range(len(v)-1):
                if v[i] == v[i+1] == 1:
                    flag = 1
            if flag == 0:
                goto = []
                for i in range(W):
                    goto.append(i)
                for i in range(len(v)):
                    if v[i] == 1:
                        tmp = goto[i]
                        goto[i] = goto[i+1]
                        goto[i+1] = tmp
                #print(goto)        
                for i in range(W):
                    for j in range(W):
                        dp[h][i][goto[j]] += dp[h-1][i][j]
                        dp[h][i][goto[j]] %= mod
        #print(dp)
    print(dp[H][0][K-1])
            
    
main()