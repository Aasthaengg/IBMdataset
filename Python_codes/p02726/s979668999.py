def main():
    n, x, y = list(map(int, input().split()))
    l = lambda i, j: min(abs(i - j), abs(i - x) + 1 + abs(y - j), abs(i - y) + 1 + abs(x - j)) - 1
    ans = [0] * (n - 1)
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            ans[l(i, j)] += 1
    [print(a) for a in ans]

if __name__ == '__main__':
    main()
