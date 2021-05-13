# K - Stones
def main():
    N, K, *A = map(int, open(0).read().split())
    dp = [False] * (K + 1)  # dp[i] := a player can win if i stones remain in their turn. (dp[0] := lose)
    for i in range(K):
        if dp[i]:
            continue
        for a in A:
            if i + a > K:
                break
            dp[i + a] = True
            if dp[-1]:
                print("First")
                return
    print("Second")


if __name__ == "__main__":
    main()
