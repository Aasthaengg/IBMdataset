def main():
    n, k = map(int, input().split())
    cnt = 0
    i = 1
    # nãå¤§ãã
    while n >= i:
        i *= k
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()