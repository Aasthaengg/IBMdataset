def dfs(i):
    global t
    t += 1
    D[i] = t
    for e in es[i]:
        if D[e] == 0:
            dfs(e)
    t += 1
    F[i] = t


if __name__ == "__main__":
    N = int(input())
    es = [[] for _ in range(N+1)]
    for _ in range(N):
        ipts = [int(ipt) for ipt in input().split()]
        if ipts[1] > 0:
            es[ipts[0]] = ipts[2:]
    D = [0 for _ in range(N+1)]
    F = [0 for _ in range(N+1)]
    t = 0
    for i in range(1, N+1):
        if D[i] == 0:
            dfs(i)
    for i in range(1, N+1):
        print(i, D[i], F[i])
