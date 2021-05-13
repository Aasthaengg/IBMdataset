import sys
def main():
    input = sys.stdin.readline
    N,M=map(int, input().split())
    A,B,C=[],[],[]
    for _ in range(M):
        a,b=map(int, input().split())
        A.append(a)
        B.append(b-1)
        C.append(list(map(lambda x:int(x)-1, input().split())))

    #dp[i][j]=i番目の鍵まで見たとき、jの宝箱を開けられるようになった場合の費用の最小値
    dp = [[10**9] * (1<<N) for _ in range(M+1)]
    dp[0][0] = 0

    for i in range(M):
        ni = i + 1
        nj = 0
        for c in C[i]: nj |= 1 << c
        for j in range(1<<N):
            dp[ni][j] = min(dp[ni][j], dp[i][j])
            dp[ni][j|nj] = min(dp[ni][j|nj], dp[i][j] + A[i])

    print(dp[M][(1<<N)-1] if dp[M][(1<<N)-1] < 10**9 else -1)

if __name__ == '__main__':
    main()