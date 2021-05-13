N, M = map(int, input().split())

Done = [False] * N
W = [0] * N
AC = 0
WA = 0
for _ in range(M):
    p, S = input().split()
    p = int(p) - 1
    if Done[p]:
        continue
    else:
        if S == 'WA':
            W[p] += 1
        else:
            AC += 1
            WA += W[p]
            Done[p] = True
print(AC, WA)
