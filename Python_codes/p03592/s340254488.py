def solve():
    N, M, K = map(int, input().split())

    for i in range(0, N+1):
        for j in range(0, M+1):

            if i*(M-j) + j*(N-i) == K:
                print("Yes")
                return

    print("No")

solve()