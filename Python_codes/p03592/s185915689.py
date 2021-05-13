def main():
    N, M, K = (int(i) for i in input().split())
    for i in range(N+1):
        for j in range(M+1):
            cur = i*j + (N-i)*(M-j)
            if cur == K:
                return print("Yes")
    print("No")


if __name__ == '__main__':
    main()
