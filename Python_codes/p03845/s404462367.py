def solve():
    N = int(input())
    T = [int(i) for i in input().split()]
    M = int(input())
    t = sum(T)
    for i in range(M):
        P, X = [int(x) for x in input().split()]
        print(t - T[P - 1] + X)

if __name__ == "__main__":
    solve()