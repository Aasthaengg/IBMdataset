import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(1000000000)

N, A, B, C = map(int, input().split())

L = [0] * N
l = []
for _ in range(N):
    L[_] = int(input())
for _ in range(4):
    l.append(_)

X = []
ans = float('inf')


def clear(X):
    global ans
    if len(X) == N:
        Z = [0]*4
        Znum = [0]*4
        for num, i in enumerate(X):
            Znum[i] += 1
            Z[i] += L[num]
        if 0 in Znum[1:]:
            return True
        ansi = abs(A - Z[1]) + abs(B - Z[2]) + abs(C - Z[3]) + (N - Znum[0] - 3) * 10
        ans = min(ans, ansi)
        return True
    else:
        for j in range(4):
            X.append(l[j])
            clear(X)
            X.pop()


clear(X)
print(ans)
