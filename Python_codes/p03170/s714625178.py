def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [False] * (K+1)
    for i in range(K+1):
        for hop in a:
            if i - hop >= 0:
                if dp[i - hop] is False:
                    dp[i] = True
                    break
    if dp[-1]:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
