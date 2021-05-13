def resolve():
    N = int(input())
    D, X = list(map(int, input().split()))
    A = [int(input()) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(201 + 1):
            if j * A[i] + 1 <= D:
                ans += 1

    print(ans+X)
    return


resolve()