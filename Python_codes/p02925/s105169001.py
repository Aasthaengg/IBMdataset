import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n = int(input())
    A = [None] * n
    for i in range(n):
        tmp = list(map(lambda x:int(x) - 1, input().split()))
        tmp.reverse()
        A[i] = tmp

    now = set()
    for i in range(n):
        j = A[i][-1]
        if i == A[j][-1]:
            now.add((min(i, j), max(i, j)))

    cnt = 0
    while now:
        next = set()
        for i, j in now:
            A[i].pop()
            A[j].pop()

        for i0, i1 in now:
            for i in (i0, i1):
                if not A[i]:
                    continue
                j = A[i][-1]
                if not A[j]:
                    continue
                if i == A[j][-1]:
                    next.add((min(i, j), max(i, j)))

        now = next
        cnt += 1

    if any(row for row in A):
        print(-1)
        return
    print(cnt)
resolve()