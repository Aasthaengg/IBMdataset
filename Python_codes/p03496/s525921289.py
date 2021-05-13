import sys

sys.setrecursionlimit(10000)
INF = float('inf')


def ok(li):
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            return False
    return True


def print_ans(start):
    print(N * 2)
    for y in range(start, N):
        x = max(start, y - 1)
        print(x + 1, y + 1)
        print(x + 1, y + 1)
    for y in reversed(range(0, start)):
        x = min(start - 1, y + 1)
        print(x + 1, y + 1)
        print(x + 1, y + 1)


N = int(input())
A = list(map(int, input().split()))

for start in range(N + 1):
    result = A.copy()
    # 右に足してく
    for y in range(start, N):
        x = max(start, y - 1)
        result[y] += result[x] * 2
    # 左に足してく
    for y in reversed(range(0, start)):
        x = min(start - 1, y + 1)
        result[y] += result[x] * 2
    if ok(result):
        print_ans(start)
        break
