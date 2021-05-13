def solve():
    n, m = map(int, input().split())
    u = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        u[a - 1] += 1
        u[b - 1] += 1
    for i in range(n):
        print(u[i])


if __name__ == '__main__':
    solve()