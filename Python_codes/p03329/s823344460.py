def main():
    N = int(input())
    dp = [-1]*(N + 1)
    dp[0] = 0
    multiples = [1]
    n = 9
    while n <= N:
        multiples.append(n)
        n *= 9
    n = 6
    while n <= N:
        multiples.append(n)
        n *= 6
    multiples.sort(reverse=True)
    # print(multiples)
    for ratio in reversed(multiples):
        for i in range(N + 1):
            c = dp[i]
            if c == - 1:
                continue
            if i + ratio > N:
                continue
            if dp[i + ratio] == -1 or dp[i + ratio] > c + 1:
                dp[i + ratio] = c + 1
    # print(dp)
    print(dp[N])

if __name__ == '__main__':
    main()
