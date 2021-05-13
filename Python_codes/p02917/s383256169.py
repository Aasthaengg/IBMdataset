def solve():
    N = int(input())
    B = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        if i == 0:
            ans += B[0]
        elif i == N - 1:
            ans += B[N - 2]
        else:
            ans += min(B[i - 1], B[i])
    print(ans)


if __name__ == "__main__":
    solve()