def main() -> None:
    A, B = map(int, input().split())
    now, cnt = 1, 0
    while True:
        if now >= B:
            break
        now += A - 1
        cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
