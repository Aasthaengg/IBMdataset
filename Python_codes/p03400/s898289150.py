def solve():
    N = int(input())
    D, X = map(int, input().split())
    ans = X
    A = [int(input()) for _ in range(N)]
    for a in A:
        d = 1
        while d <= D:
            ans += 1
            d += a
    print(ans)



if __name__ == "__main__":
    solve()