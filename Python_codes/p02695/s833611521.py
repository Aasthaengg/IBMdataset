from itertools import combinations
N, M, Q = map(int, input().split())
A = []
for i in range(Q):
    A.append(list(map(int, input().split())))

ans = 0
for c in combinations(range(N+M-1), N):
    x = sorted(list(c))
    ans_new = 0
    for i in range(Q):
        if x[A[i][1]-1] - A[i][1] - x[A[i][0]-1] + A[i][0] == A[i][2]:
            ans_new += A[i][3]
    if ans_new > ans:
        ans = ans_new
print(ans)