def main():
    a, b, c = map(int, input().split())
    if a == b and b == c:
        print(-1 if a % 2 == 0 else 0)
        return
    cnt = 0
    for i in range(10 ** 9):
        if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
            break
        a, b, c = (b + c) // 2, (a + c) // 2, (a + b) // 2
        cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
