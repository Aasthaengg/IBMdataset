def getval():
    s = input()
    return s
    
def main(s):
    #dp for "a","ab","abc"
    mod = 10**9 + 7
    dp = [0,0,0,0]
    p3 = [1]
    for i in range(len(s)):
        p3.append((3*p3[i])%mod)
    for i in s:
        if i=="A":
            dp[0] += p3[dp[3]]
            dp[0] %= mod
        elif i=="B":
            dp[1] += dp[0]
            dp[1] %= mod
        elif i=="C":
            dp[2] += dp[1]
            dp[2] %= mod
        else:
            temp1 = dp[0]*2
            temp2 = dp[1]*2
            temp3 = dp[2]*2
            dp[2] += dp[1]
            dp[1] += dp[0]
            dp[0] += p3[dp[3]]
            dp[2] += temp3
            dp[1] += temp2
            dp[0] += temp1
            dp[3] += 1
            for j in range(3):
                dp[j] %= mod
            #print(dp)
    print(dp[2])

if __name__=="__main__":
    s = getval()
    main(s)