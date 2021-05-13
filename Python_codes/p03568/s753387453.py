N = int(input())
A = list(map(int, input().split()))


T = [None] * N

c = 0

from functools import reduce

def check():
    def f(a, b):
        return a * b

    global c
    r = reduce(f, T)
    # print(T, r)
    if r % 2 == 0:
        c += 1


def dfs(pos):
    if pos == N:
        check()
        return

    T[pos] = A[pos] - 1
    dfs(pos+1)

    T[pos] = A[pos]
    dfs(pos+1)

    T[pos] = A[pos] + 1
    dfs(pos+1)

dfs(0)

print(c)