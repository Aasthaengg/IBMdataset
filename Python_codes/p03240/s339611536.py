def solve():
    n = int(input())
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    h = [0 for _ in range(n)]
    for i in range(n):
        x[i], y[i], h[i] = map(int, input().split())
        if h[i]:
            xn, yn, hn = x[i], y[i], h[i]

    for cx in range(101):
        for cy in range(101):
            H = hn + abs(xn - cx) + abs(yn - cy)
            if all(h[i] == max(H - abs(x[i] - cx) - abs(y[i] - cy), 0) for i in range(n)):
                print(cx, cy, H)


if __name__ == '__main__':
    solve()
