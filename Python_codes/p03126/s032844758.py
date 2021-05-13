def solve():
    n, m = map(int, input().split())
    f = [0] * (m+1)
    for _ in range(n):
        k, *a = map(int, input().split())
        for i in a:
            f[i] += 1
    print(f.count(n))


if __name__ == '__main__':
    solve()
