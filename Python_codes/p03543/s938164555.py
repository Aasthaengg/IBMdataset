def solve():
    N = input()
    if len(set(N[:3])) == 1 or len(set(N[1:])) == 1:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    solve()
