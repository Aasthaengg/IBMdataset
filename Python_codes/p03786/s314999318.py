def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    S = [0] * N  # 累積和
    S[0] = A[0]
    for n in range(1, N):
        S[n] = S[n - 1] + A[n]
    n = N - 2
    while n >= 0:
        if 2 * S[n] < A[n + 1]:  # A_n までの数字で A_(n+1)を吸収できない
            break
        n -= 1
    print(N - 1 - n)


if __name__ == '__main__':
    main()
