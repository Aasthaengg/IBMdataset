def main():
    A, B = map(int, input().split())
    ans = 0
    if B == 1:
        print(0)
        exit()
    while True:
        ans += 1
        if (A - 1) * ans + 1 >= B:
            break
    print(ans)


if __name__ == '__main__':
    main()
