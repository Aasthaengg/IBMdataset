def main():
    NK = list(map(int, input().split()))
    N, K = NK[0], NK[1]
    ans = 0
    while N >= K:
        N = N - 1
        ans += 1
    print(ans)
main()