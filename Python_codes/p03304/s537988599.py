def solve():
    n, m, d = map(int, input().split())
    if d == 0:
        print((m-1)/n)
    else:
        print(2*(m-1)*(n - d)/(n**2))

if __name__ == '__main__':
    solve()