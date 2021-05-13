def main():
    N, M = map(int, input().split())
    A = [int(a) for a in input().split()]
    d1 = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

    # for a given number of matches, give the largest digit
    d2 = dict()
    for a in A:
        if d1[a] not in d2: d2[d1[a]] = a
        else: d2[d1[a]] = max(a, d2[d1[a]])

    # for these digit, give the match count
    lv = []
    for a in d2.values(): lv.append(a)

    dp = [None for _ in range(N+1)]
    dp[0] = ""
    for i in range(1, N+1):
        for a in lv:
            j = i - d1[a]
            if j >= 0 and dp[j] != None:
                if dp[i] == None:
                    dp[i] = dp[j] + str(a)
                elif len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + str(a)
                elif len(dp[i]) == len(dp[j]) + 1:
                    dp[i] = max(dp[i], dp[j] + str(a))
                # print(dp[i], i)
    # print(dp)
    return dp[N]




if __name__ == '__main__':
    print(main())