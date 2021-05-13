def main():
    N = int(input())
    *A, = map(int, input().split())
    *B, = map(int, input().split())

    ans = 0
    for i in range(N):
        beaten = min(A[i], B[i])
        A[i] -= beaten
        B[i] -= beaten
        ans += beaten

        if B[i]:
            beaten = min(A[i + 1], B[i])
            A[i + 1] -= beaten
            B[i] -= beaten
            ans += beaten

    print(ans)


if __name__ == '__main__':
    main()
