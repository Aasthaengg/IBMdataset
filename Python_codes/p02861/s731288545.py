from itertools import permutations

def solve():
    N = int(input())
    P = [[int(i) for i in input().split()] for _ in range(N)]
    tmp = 0
    c = 0
    for p in permutations(P):
        t = 0
        c += 1
        for i in range(N - 1):
            t += ((p[i][0] - p[i + 1][0]) ** 2 + (p[i][1] - p[i + 1][1]) ** 2) ** 0.5
        tmp += t
    print(tmp / c)

if __name__ == "__main__":
    solve()
