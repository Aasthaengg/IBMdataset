N, W = map(int, input().split())
wv = []
for _ in range(N):
    w, v = map(int, input().split())
    wv.append((w, v))
memo = [{} for _ in range(N + 1)]


def f(i, j):
    if 0 >= i or 0 >= j:
        return 0
    if j in memo[i]:
        return memo[i][j]
    w, v = wv[i - 1]
    t = f(i - 1, j)
    if j - w >= 0:
        t = max(t, f(i - 1, j - w) + v)
    memo[i][j] = t
    return t


def main():
    print(f(N, W))


main()
