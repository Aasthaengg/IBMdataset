def solve():
    h, n = map(int, input().split())
    a = map(int, input().split())
    for i in a:
        h -= i
    print('YNeos'[h>0::2])


if __name__ == '__main__':
    solve()
