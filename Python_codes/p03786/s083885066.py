def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0]*(N-1)
    B[0] = A[0]
    for i in range(1, N - 1):
        B[i] = B[i - 1] + A[i]
    i = N - 2
    # print(A, B)
    while i >= 0:
        if A[i + 1] <= B[i] * 2:
            i -= 1
        else:
            break
    print(N - i - 1)


if __name__ == '__main__':
    main()
