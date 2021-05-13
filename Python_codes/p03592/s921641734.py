def main():
    N, M, K = map(int, input().split())
    ok = False
    for i in range(N+1):
        for j in range(M+1):
            if K == i*(M-j) + j*(N-i):
                ok = True
                break
    print("Yes" if ok else "No")
         


if __name__ == "__main__":
    main()