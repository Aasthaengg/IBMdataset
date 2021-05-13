#!python3

LI = lambda: list(map(int, input().split()))

# input
N, M = LI()
AB = [LI() for _ in range(N)]
CD = [LI() for _ in range(M)]

INF = 10 ** 15


def distance(i, j):
    d = abs(AB[i][0] - CD[j][0]) + abs(AB[i][1] - CD[j][1])
    return d


def solve(i):
    # distance, number
    w = (INF, INF)
    for j in range(M):
        t = (distance(i, j), j + 1)
        w = min(w, t)
    return w[1]


def main():
    for i in range(N):
        ans = solve(i)
        print(ans)
    
    
if __name__ == "__main__":
    main()
