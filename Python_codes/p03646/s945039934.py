# ABC068D - Decrease (Contestant ver.) (ARC079D)
def main():
    K = int(input())
    N, A, r = 50, [49 + K // 50] * 50, K % 50
    for i in range(N):
        A[i] += N - r + 1 if i < r else -r
    print(N)
    print(*A)


if __name__ == "__main__":
    main()