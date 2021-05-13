def main():
    N = int(input())

    if N % 2 == 1:
        print(0)
        return

    N //= 2

    ret = 0
    while N > 0:
        N //= 5
        ret += N
    print(ret)


if __name__ == '__main__':
    main()
