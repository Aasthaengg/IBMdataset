def solve():
    N = int(input())
    S = set(input().split())
    if len(S) == 3:
        print('Three')
    else:
        print('Four')


if __name__ == "__main__":
    solve()
