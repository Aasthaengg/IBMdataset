def main():
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())
    if N > K:
        print((K * X) + (Y * (N - K)))
    else:
        print(N * X)
main()