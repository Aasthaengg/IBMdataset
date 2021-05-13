def main():
    n, m = map(int, input().split())
    ABs = [list(map(int, input().split())) for _ in range(n)]

    ABs = sorted(ABs)
    Count = 0
    ans = 0
    for i in range(n):
        if Count == m:
            break
        if ABs[i][1] + Count <= m:
            ans += ABs[i][0] * ABs[i][1]
            Count += ABs[i][1]
        else:
            o = m - Count
            ans += ABs[i][0] * o
            Count += o

    print(ans)


if __name__ == "__main__":
    main()
