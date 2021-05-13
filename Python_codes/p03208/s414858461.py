def solve():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    hk = [h[i+k-1] - h[i] for i in range(n - k + 1)]
    print(min(hk))

if __name__ == '__main__':
    solve()
