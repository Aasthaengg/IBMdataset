import sys

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [[int(a) for a in input().split()] for _ in range(N)]
    C = [[int(c) for c in input().split()] for _ in range(M)]
    Ans = [1] * N
    for i in range(N):
        a, b = S[i]
        dist = abs(a - C[0][0]) + abs(b - C[0][1])
        for j in range(1, M):
            tdist = abs(a - C[j][0]) + abs(b - C[j][1])
            if tdist < dist:
                dist = tdist
                Ans[i] = j + 1
    print(*Ans, sep="\n")
    return 0

if __name__ == "__main__":
    solve()