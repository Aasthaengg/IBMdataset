def solve():
    A, B = map(int, input().split())
    if A + B < 10:
        print(A + B)
    else:
        print('error')


if __name__ == "__main__":
    solve()