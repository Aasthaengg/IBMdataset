def main():
    # n = int(input())
    n, k = map(int, input().split())
    # h = list(map(int, input().split()))
    # s = input()

    ans = 0
    while True:
        if (n - 1) * ans + 1 >= k:
            print(ans)
            break
        ans += 1


if __name__ == '__main__':
    main()
