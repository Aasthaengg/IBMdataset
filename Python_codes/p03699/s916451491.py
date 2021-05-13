def main():
    N = int(input())
    S = [int(input()) for _ in range(N)]
    total = sum(S)
    if total % 10 != 0:
        print(total)
        exit()
    for s in sorted(S):
        if s % 10 != 0:
            print(total - s)
            exit()
    print(0)


if __name__ == '__main__':
    main()
