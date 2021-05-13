def sol():
    n, k = map(int, input().split())
    ps = list(map(int, input().split()))
    sort_ps = sorted(ps)
    ans = 0
    for i in range(k):
        ans += sort_ps[i]
    print(ans)
if __name__ == "__main__":
    sol()
