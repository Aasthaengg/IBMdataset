def main():
    N = int(input())
    S = input()
    # flags[n][m]: n 番目の文字と同じ文字がその m 個後にあれば1
    flags = [[0] * N for _ in range(N)]
    for n, c in enumerate(S):
        for m in range(1, N - n):
            if c == S[n + m]:
                flags[n][m] = 1
    ans = 0
    for m in range(1, N):
        from_n = -1
        for to_n in range(N):
            if flags[to_n][m] == 0:
                ans = max(ans, min(m, to_n - from_n - 1))
                from_n = to_n
        if from_n != to_n:
            ans = max(ans, min(m, to_n - from_n - 1))
    print(ans)


if __name__ == '__main__':
    main()