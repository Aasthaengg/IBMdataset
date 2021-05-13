def solve():
    N = int(input())
    s = [int(input()) for _ in range(N)]
    sm = sum(s)
    dp = [False] * (sm + 1)
    dp[0] = True

    for val in s:
        for i in range(sm, -1, -1):
            if dp[i] and i+val <= sm:
                dp[i+val] = True
    
    for i in range(sm, -1, -1):
        if dp[i] and i % 10 != 0:
            print(i)
            return
    else:
        print(0)

if __name__ == '__main__':
    solve()