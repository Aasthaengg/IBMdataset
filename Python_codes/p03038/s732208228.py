N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
bc = [0] * M
for i in range(M):
    bc[i] = list(map(int, input().split()))

bc = sorted(bc, key= lambda x: x[1], reverse=True)

n = 0
f = 0
for i in range(M):
    for j in range(bc[i][0]):
        if A[n] < bc[i][1]:
            A[n] = bc[i][1]
            n += 1
            if n == N:
                f = 1
                break
        else:
            f = 1
    if f == 1:
        break

print(sum(A))