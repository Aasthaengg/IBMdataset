def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    ans = 0
    r = A[0]
    for i in range(1, N + 1):
        a = A[i]
        b = B[i - 1]
        ans += min(r + a, b)
        r = max(min(r + a - b, a), 0)
    print(ans)

if __name__ == "__main__":
    solve()
