def solve():
    N, M = [int(i) for i in input().split()]
    R = [[] for _ in range(N)]
    for _ in range(M):
        a, b = [int(i) for i in input().split()]
        R[a - 1].append(b)
        R[b - 1].append(a)
    for r in R:
        print(len(r))

if __name__ == "__main__":
    solve()