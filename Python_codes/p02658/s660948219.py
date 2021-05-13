def main() -> None:
    n = int(input())
    a_tuple = tuple(map(int, input().split()))

    if 0 in a_tuple:
        print(0)
        return
    boader = 10 ** 18
    answer = 1
    for a in a_tuple:
        answer *= a
        if answer > boader:
            print(-1)
            return
    print(answer)


if __name__ == '__main__':
    main()
