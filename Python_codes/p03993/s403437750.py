def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        if i + 1 == A[A[i] - 1]:
            ans += 1
    print(ans // 2)

if __name__ == "__main__":
    solve()
