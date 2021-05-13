def main():
    N = int(input())
    A = list(map(int, input().split()))

    res = 1
    for a in A:
        if a % 2 == 0:
            res *= 2

    print(3**N - res)


if __name__ == "__main__":
    main()
