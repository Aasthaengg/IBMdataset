import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
si, res = [1] + [0 for i in range(55)], 0
a, b, c, d = [0 for i in range(55)], [0 for i in range(55)], [0 for i in range(55)], [0 for i in range(55)]
for i in range(1, q+1): a[i], b[i], c[i], d[i] = map(int, input().split())

def solve(x: int):
    global res
    if x == n + 1: res = max(res, sum([d[i] for i in range(1, q+1) if si[b[i]] - si[a[i]] == c[i]]))
    else:
        for i in range(si[x-1], m + 1): si[x] = i; solve(x+1)
solve(1); print(res)