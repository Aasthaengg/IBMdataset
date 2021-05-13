def solve():
    a, b = map(int, input().split())
    n = a + b
    if n % 2 == 0:
        print((a+b)//2)
    else:
        print('IMPOSSIBLE')


if __name__ == '__main__':
    solve()
