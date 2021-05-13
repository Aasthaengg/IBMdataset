import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    MOD = 10**9 + 7
    SI = lambda : sys.stdin.readline().rstrip()
    S = SI()

    dp = [[0] * 4 for _ in range(len(S)+1)]
    dp[0] = [1,0,0,0]
    ans = 0
    for i in range(len(S)):
        rg = [0,1,2] if S[i] == '?' else [ord(S[i])-ord('A')]
        for a in rg:
            for b in range(4):
                if a == b:
                    c = b + 1
                    dp[i + 1][c] = (dp[i + 1][c] + dp[i][b]) % MOD
                dp[i + 1][b] = (dp[i + 1][b] + dp[i][b]) % MOD

    print(dp[-1][-1])

if __name__ == '__main__':
    main()