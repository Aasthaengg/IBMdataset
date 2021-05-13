def main():
    N = int(input())

    ma = 0
    tot = 0
    while tot < N:
        ma += 1
        tot += ma

    skip = tot - N
    ans = {x for x in range(1, ma + 1) if x != skip}

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
