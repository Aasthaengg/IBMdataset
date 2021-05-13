# ABC090D - Remainder Reminder (ARC091D)
def main():
    N, K = tuple(map(int, input().split()))
    if K == 0:
        print(N ** 2)
        return
    ans = 0
    for i in range(K + 1, N + 1):
        ans += N // i * (i - K) + max(0, (N % i) - K + 1)
    print(ans)


if __name__ == "__main__":
    main()