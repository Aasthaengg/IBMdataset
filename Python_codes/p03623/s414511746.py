def solve():
    x, a, b = map(int, input().split())
    if abs(x-a) > abs(x-b):
        print('B')
    else:
        print('A')


if __name__ == "__main__":
    solve()
