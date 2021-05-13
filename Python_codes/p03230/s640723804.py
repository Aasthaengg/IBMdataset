def grid(N):
    n = 0
    while n * (n + 1) < N * 2:
        n += 1

    if n * (n + 1) != N * 2:
        print("No")
        return

    S = [[0]*n for _ in range(n+1)]
    cnt = 1
    for i in range(n+1):
        for j in range(n):
            if i <= j:
                S[i][j] = cnt
                cnt += 1
            else:
                S[i][j] = S[j][i-1]
    print("Yes")
    print(len(S))
    for s in S:
        print(n, end=" ")
        print(*s, sep=" ")


if __name__ == "__main__":
    N = int(input())
    grid(N)
