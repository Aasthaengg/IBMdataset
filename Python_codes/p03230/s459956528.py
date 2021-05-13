N = int(input())
K = 0
for i in range(1, 500):
    if i * (i + 1) == 2 * N:
        K = i
        break
if K == 0:
    print("No")
    exit()

A = [[0] * K for _ in range(K)]
count = 1
for i in range(K):
    for j in range(i + 1):
        A[i][j] = count
        count += 1

print("Yes")
print(K + 1)
ans = []
for i in range(K):
    tmp = A[i][:i + 1]
    for y in range(i + 1, K):
        tmp.append(A[y][i])
    ans.append(tmp)
ans.append([A[i][i] for i in range(K)])
for a in ans:
    print(K, *a)