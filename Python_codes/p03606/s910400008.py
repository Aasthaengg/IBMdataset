def main():
    n = int(input())
    lrs = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for l, r in lrs:
        ans += r - l + 1
    print(ans)


if __name__ == "__main__":
    main()
