def solve():
    A, B, C = map(int, input().split())
    if A <= C <= B:
        print('Yes')
    else:
        print("No")


if __name__ == "__main__":
    solve()