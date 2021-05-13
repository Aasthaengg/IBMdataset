def main():
    N = int(input())
    P = [int(input()) for _ in range(N)]
    seq = [0] * (N+2)
    for p in P:
        seq[p] = seq[p-1] + 1
    print(N - max(seq))


if __name__ == "__main__":
    main()
