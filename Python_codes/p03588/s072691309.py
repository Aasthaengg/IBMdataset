def main():
    N = int(input())
    A = [[int(i) for i in input().split()] for j in range(N)]
    mi = 0
    idx = 0
    for a, b in A:
        if mi < a:
            mi = a
            idx = b
    print(mi + idx)


if __name__ == '__main__':
    main()
