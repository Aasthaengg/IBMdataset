def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    L = [0]*(N+1)
    for i, a in enumerate(A, start=1):
        L[i] = max(L[i-1], a)

    R = [0]*(N+2)
    for i in range(N)[::-1]:
        R[i] = max(R[i+1], A[i])

    for i in range(N):
        print(max(L[i], R[i+1]))


if __name__ == '__main__':
    main()
