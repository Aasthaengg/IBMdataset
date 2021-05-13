def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N = ii()
    S = input()
    dp = [0]*N
    dp[0] = S[1:].count('W')
    for i in range(1, N):
        dp[i] = dp[i-1]
        if S[i-1] == 'E':
            dp[i] += 1
        if S[i] == 'W':
            dp[i] -= 1
    print(N-1-max(dp)) 
    


if __name__ == '__main__':
    main()
