def func():
    pass


def main():
    n, k = map(int, input().split())

    mx = (n + 1) // 2
    if mx >= k:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
