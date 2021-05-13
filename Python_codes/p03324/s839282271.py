def solve(D, N):
    if N < 100:
        ans = 100**D * N
    else:
        ans = 100**D*101

    return ans


if __name__ == "__main__":
    D, N = map(int, input().split())
    print(solve(D, N))
