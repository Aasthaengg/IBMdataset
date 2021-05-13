import copy

N, M, Q = [int(_) for _ in input().split()]
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q

for i in range(Q):
    xs = [int(_) for _ in input().split()]
    a[i] = xs[0] - 1
    b[i] = xs[1] - 1
    c[i] = xs[2]
    d[i] = xs[3]


def calc_score(A):
    acc = 0
    for i in range(Q):
        if c[i] == A[b[i]] - A[a[i]]:
            acc += d[i]
    return acc


max_score = -1


def dfs(A):
    if len(A) == N:
        global max_score
        max_score = max(calc_score(A), max_score)
    else:
        if len(A) == 0:
            A.append(1)
        else:
            A.append(A[-1])
        while (A[-1] <= M):
            dfs(copy.deepcopy(A))
            A[-1] += 1


dfs([])
print(max_score)
