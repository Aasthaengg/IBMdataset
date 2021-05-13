def main():
    N = int(input())
    S = input()
    west_counts = [0 for _ in range(N)]
    east_counts = [0 for _ in range(N)]
    for i, c in enumerate(S):
        if c == 'W':
            west_counts[i] = 1
        else:
            east_counts[i] = 1
    for i in range(1, N):
        west_counts[i] += west_counts[i - 1]  # cumsum from leftside
        east_counts[N - 1 - i] += east_counts[N - i]  # cumsum from rightside
    ans = N
    for i in range(N):
        d = 0
        if i < N - 1:
            d += east_counts[i + 1]  # rightside
        if i > 0:
            d += west_counts[i - 1]  # leftside
        ans = min([ans, d])
    print(ans)


if __name__ == '__main__':
    main()