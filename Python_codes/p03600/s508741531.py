from copy import deepcopy
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = deepcopy(A)

s = 0
for i in range(N):
    via = A[i]
    for j in range(N):
        start = A[j]
        for k in range(N):
            if start[k] > start[i]+via[k]:
                print(-1)
                exit()

for j in range(N):
    for k in range(j):
        a = A[j][k]
        for i in range(N):
            if i in {j, k}:
                continue
            if a == A[j][i]+A[i][k]:
                break
        else:
            s += a
            # print(j,k,a)
print(s)