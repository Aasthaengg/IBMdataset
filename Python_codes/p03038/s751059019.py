N, M = map(int, input().split())
A = list(map(lambda x: int(x), input().split()))
Q = []

for i in range(M):
    Q.append(tuple(map(int, input().split())))

A.sort()

Q.sort(key=lambda x: x[1], reverse=True)

cur = 0
for i in range(M):
    cnt = Q[i][0]
    while cnt > 0 and cur < N:
        if A[cur] >= Q[i][1]:
            break
        A[cur] = Q[i][1]
        cur += 1
        cnt -= 1

print(sum(A))