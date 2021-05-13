def main():
    N, K = map(int, input().split())
    *A, = map(int, input().split())

    for _ in range(K):
        B = [0] * (N + 1)
        for i, x in enumerate(A):
            B[max(0, i - x)] += 1
            B[min(N - 1, i + x) + 1] -= 1
        for i in range(N):
            B[i + 1] += B[i]
        B.pop()
        if A == B: break
        A = B
    print(*A)


if __name__ == '__main__':
    main()
