def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    avg = sum(A)/N
    mi = abs(A[0] - avg)
    idx = 0
    for i, a in enumerate(A[1:], start=1):
        if abs(a - avg) < mi:
            mi = abs(a - avg)
            idx = i
    print(idx)


if __name__ == '__main__':
    main()
