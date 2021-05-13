import sys

if __name__ == "__main__":
    N, M, K = [int(x) for x in input().split(" ")]
    if M < N:
        N, M = M, N
    for x in range(0, N + 1):
        for y in range(0, M + 1):
            if x * (M - y) + (y * (N - x)) == K:
                print("Yes")
                sys.exit(0)
    print("No")
