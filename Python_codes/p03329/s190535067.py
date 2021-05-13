def main():
    N = int(input())
    amounts = [1]
    lim = 10**6
    mul6 = 6
    while mul6 < lim:
        amounts.append(mul6)
        mul6 *= 6
    mul9 = 9
    while mul9 < lim:
        amounts.append(mul9)
        mul9 *= 9
    
    dp = [lim] * (N+1)
    dp[0] = 0
    for i in range(N):
        for a in amounts:
            if i+a <= N:
                dp[i+a] = min(dp[i+a],dp[i]+1)
    print(dp[N])

    



main()