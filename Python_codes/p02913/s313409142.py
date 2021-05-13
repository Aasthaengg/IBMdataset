import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    N = NI()
    S = SI()
    dp = [[0] * (N+1) for _ in range(N)]

    ans = 0
    for i in range(1,N):
        for j in range(i+1,N+1):
            if S[i-1] == S[j-1]:
                if j-i > dp[i-1][j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ans = max(ans,dp[i][j])
                else:
                    dp[i][j] = 1
    print(ans)

if __name__ == '__main__':
    main()