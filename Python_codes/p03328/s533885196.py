def solve():
    a, b = map(int, input().split())
    d = b - a
    sumb = 0
    for i in range(d):
        sumb += i + 1
    print(sumb - b)


if __name__ == "__main__":
    solve()
