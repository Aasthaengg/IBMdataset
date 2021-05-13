def main():
    import sys
    input = sys.stdin.buffer.readline
    N, M = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    A.sort(reverse=True)
    dp = ["-"]*(N+10)
    dp[0] = ""
    match = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    for i in range(N+1):
        if dp[i] == "-":
            continue
        for a in A:
            cur = dp[i+match[a]]
            ne = dp[i] + str(a)
            if len(cur) < len(ne) or cur < ne:
                dp[i+match[a]] = ne
    # print(dp)
    print(dp[N])


if __name__ == '__main__':
    main()
