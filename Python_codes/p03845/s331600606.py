N = int(input())
T = list(map(int, input().split()))
M = int(input())
P = [list(map(int, input().split())) for _ in range(M)]
for p in P:
    copy_p = T.copy()
    copy_p[p[0] - 1] = p[1]
    print(sum(copy_p))