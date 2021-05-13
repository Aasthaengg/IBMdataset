def main():
    a, b = map(int, input().split())
    cnt = 1
    ans = 0

    while True:
        if cnt >= b:
            break
        cnt += a - 1
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
