def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += min(B[i], A[i] + A[i + 1])
        A[i + 1] = min(A[i + 1], max(A[i] + A[i + 1] - B[i], 0))
    print(ans)


solve()
