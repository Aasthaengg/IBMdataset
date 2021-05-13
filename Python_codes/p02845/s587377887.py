def main():
    n = int(input())
    a = list(map(int, input().split()))
    colors = [[0 for _ in range(3)] for _ in range(n + 1)]
    # color 1, 2, 3
    ans = 1
    mod = 10 ** 9 + 7
    for i in range(n):
        for j in range(3):
            colors[i + 1][j] = colors[i][j]
        for j in range(3):
            if a[i] == colors[i + 1][j]:
                colors[i + 1][j] += 1
                break
    for i in range(n):
        ans *= colors[i].count(a[i])
        ans %= mod
    print(ans)


if __name__ == '__main__':
    main()

