def solve():
    k, x = map(int, input().split())
    print('YNeos'[500*k<x::2])

if __name__ == '__main__':
    solve()
