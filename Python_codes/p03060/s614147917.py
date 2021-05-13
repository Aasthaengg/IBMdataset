import sys


def solve(i, x, y):
    if i == N:
        global max_ans
        max_ans = max(max_ans, x-y)
        return
    solve(i+1, x, y)
    solve(i+1, x+V[i], y+C[i])


sys.setrecursionlimit(2**20)
N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
max_ans = 0
solve(0, 0, 0)
print(max_ans)