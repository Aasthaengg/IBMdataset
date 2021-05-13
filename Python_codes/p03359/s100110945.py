def solve():
    a, b = map(int, input().split())
    if b >= a:
        print(a)
    else:
        print(a - 1)


if __name__ == "__main__":
    solve()
