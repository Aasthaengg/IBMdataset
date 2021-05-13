def main():
    n, k = map(int, input().split())
    hs = sorted([int(input()) for _ in range(n)])
    ans = float("inf")
    for i in range(n-k+1):
        ans = min(ans, hs[i+k-1]-hs[i])
    print(ans)


if __name__ == "__main__":
    main()
