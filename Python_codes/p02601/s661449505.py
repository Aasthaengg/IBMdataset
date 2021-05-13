def main():
    A, B, C = map(int, input().split())
    K = int(input())

    cnt = 0
    while A >= B:
        B *= 2
        cnt += 1
    while B >= C:
        C *= 2
        cnt += 1
    print('Yes' if cnt <= K else 'No')


if __name__ == '__main__':
    main()
