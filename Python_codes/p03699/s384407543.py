def main():
    N = int(input())
    S = [int(input()) for _ in range(N)]
    S.sort()
    total = sum(S)
    if total % 10 != 0:
        print(total)
    else:
        for s in S:
            if s % 10 != 0:
                print(total - s)
                return
        print(0)


if __name__ == '__main__':
    main()