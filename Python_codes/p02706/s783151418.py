def solve():
    N,M = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    freedays = N - sum(A)
    if freedays < 0:
        print(-1)
    else:
        print(freedays)

if __name__ == "__main__":
    solve()