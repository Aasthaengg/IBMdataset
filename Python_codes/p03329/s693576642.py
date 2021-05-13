def main():
    n = int(input())
    C = [1, ]
    c = 6
    while c < 100000:
        C.append(c)
        c *= 6
    c = 9
    while c < 100000:
        C.append(c)
        c *= 9
    INF = float('inf')
    dp = [INF] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        C_filtered = [c for c in C if c <= i]
        dp[i] = min([dp[i - c] + 1 for c in C_filtered])
    print(dp[n])
if __name__ == '__main__':
    main()
