def main():
    N, K = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    dp = [False]*(K+1)

    for i in range(K):
        if dp[i]:
            continue
        for a in A:
            if K < i + a:
                continue
            dp[i + a] = True

    if dp[K]:
        print("First")
    else:
        print("Second")


if __name__ == '__main__':
    main()
