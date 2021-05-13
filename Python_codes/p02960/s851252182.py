def getval():
    s = input()
    return s

def main(s):
    mod = 10**9 + 7
    #Remainders of 10**i%13
    rem = [1]
    for i in range(11):
        rem.append((rem[-1]*10)%13)
    #Digits of ?
    arr = []
    #Sum of existing integers mod 13
    init = 0
    for i in range(len(s)):
        if s[i]=="?":
            arr.append(len(s)-i-1)
        else:
            init += (int(s[i]) * rem[(len(s)-i-1)%12])%13
            init %= 13

    #DP for number of comb such that rem is j on ith ?
    dp = [[0 for i in range(13)]]
    dp[0][0] = 1
    for i in arr:
        temp = [0 for i in range(13)]
        prev = dp[-1]
        for j in range(13):
            for k in range(10):
                update = prev[j]
                temp[(j+k*rem[i%12])%13] += update
                temp[(j+k*rem[i%12])%13] %= mod
        dp.append(temp)

    print(dp[-1][(18-init)%13])
    
                
if __name__=="__main__":
    s = getval()
    main(s)