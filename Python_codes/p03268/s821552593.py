# ARC102C - Triangular Relationship (ABC108C)
def main():
    N, K = list(map(int, input().rstrip().split()))
    a = N // K
    if K % 2 != 0:  # K: odd
        print(a ** 3)
    else:  # K: even
        b = (N + K // 2) // K
        print(a ** 3 + b ** 3)


if __name__ == "__main__":
    main()