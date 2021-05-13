def main():
    MOD = 10**9 + 7
    N = int(input())
    S = [input() for _ in range(2)]
    # pattern 0 | pattern 1
    #     X     |    XX
    #     X     |    YY
    # before | current
    #    0   |    0    -> 2
    #    0   |    1    -> 2
    #    1   |    0    -> 1
    #    1   |    1    -> 3
    before_pattern = 0 if S[0][0] == S[1][0] else 1
    ans = 3 if before_pattern == 0 else 3 * 2
    i = 1 if before_pattern == 0 else 2
    while i < N:
        pattern = 0 if S[0][i] == S[1][i] else 1
        if pattern == 0:
            if before_pattern == 0:
                ans *= 2
            i += 1
        else:
            if before_pattern == 0:
                ans *= 2
            else:
                ans *= 3
            i += 2
        before_pattern = pattern
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()