def solve():
    w, h, x, y = map(int, input().split())
    print(w * h / 2, end=' ')
    print(1 if 2*x == w and 2*y == h else 0)

if __name__ == '__main__':
    solve()