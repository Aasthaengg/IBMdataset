import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    MOD = 10**9+7
    A,T,G,C = 0,1,2,3
    dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i==A and j==G and k==C:
                    continue
                if i==A and j==C and k==G:
                    continue
                if i==G and j==A and k==C:
                    continue
                dp[3][i][j][k] = 1

    if N == 3:
        print("61")
    else:
        for n in range(4,N+1):
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        for l in range(4):
                            if i==A and j==G and k==C:
                                continue
                            if i==A and j==C and k==G:
                                continue
                            if i==G and j==A and k==C:
                                continue
                            if l==A and i==G and k==C:
                                continue
                            if l==A and j==G and k==C:
                                continue
                            dp[n][i][j][k] += dp[n-1][l][i][j]
                            dp[n][i][j][k] %= MOD
        ans = 0                    
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    ans += dp[-1][i][j][k]
        print(ans%MOD)

if __name__ == "__main__":
    main()