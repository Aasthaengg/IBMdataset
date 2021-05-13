def solve():
    x,a,b = map(int, input().split())
    xa = abs(x-a)
    xb = abs(x-b)
    print('A' if xa<xb else 'B')

if __name__ == '__main__':
    solve()