def solve():
    a, b, c = map(int, input().split())
    print([0, c-a+b][c-a+b>0])

if __name__ == '__main__':
    solve()
