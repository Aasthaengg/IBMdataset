INF = 10**9

def as_bit(ls):
    # 開けられる宝箱をbitで示す
    ret = 0
    for l in ls:
        ret |= 1 << (l - 1)
    return ret

def main():
    
    N, M = map(int, input().split())
    C, A = [], []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        c = list(map(int, input().split()))
        C.append(as_bit(c))

    dp = [[INF] * (2**N) for _ in range(M+1)]

    for i in range(M+1):
        dp[i][0] = 0

    for i in range(M):
        for bit in range(2**N):
            dp[i+1][bit|C[i]] = min(dp[i+1][bit|C[i]], dp[i][bit] + A[i])
            dp[i+1][bit] = min(dp[i+1][bit], dp[i][bit])

    ans = dp[-1][-1]
    print(ans if ans != INF else -1)

if __name__ == "__main__":
    main()
