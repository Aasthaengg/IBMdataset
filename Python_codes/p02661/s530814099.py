# E - Count Median
def main():
    N, *AB = map(int, open(0).read().split())
    A, B = AB[::2], AB[1::2]
    A.sort(), B.sort()
    mid = N // 2
    if N % 2:
        print(B[mid] - A[mid] + 1)
    else:
        print((B[mid] + B[mid - 1]) - (A[mid] + A[mid - 1]) + 1)


if __name__ == "__main__":
    main()
