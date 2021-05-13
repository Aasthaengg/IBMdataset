def main() -> None:
    N = int(input())
    ans = 0
    now, prev = 0, -1
    A = [int(x) for x in input().split()]
    for a in A:
        if a <= prev:
            now += 1
        else:
            now = 0
        prev = a
        ans = max(ans, now)
    print(ans)


if __name__ == '__main__':
    main()
