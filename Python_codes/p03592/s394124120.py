def resolve():
    n, m, k = map(int, input().split())
    for l in range(n + 1):
        for r in range(m + 1):
            black = l * m + r * n - 2 * r * l
            if black == k:
                print("Yes")
                return 0
    print("No")


if __name__ == "__main__":
    resolve()
