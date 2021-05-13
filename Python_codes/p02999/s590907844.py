def solve():
    x, a = map(int, input().split())
    print('100'[x<a::2])


if __name__ == '__main__':
    solve()
