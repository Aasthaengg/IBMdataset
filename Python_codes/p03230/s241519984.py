N = int(input())

K = int((2 * N) ** 0.5) + 1
if K * (K - 1) // 2 != N:
    print("No")
    quit()

print("Yes")
print(K)

A = [[] for _ in range(K - 1)]

cur = 1
for i in range(K - 1):
    for _ in range(i + 1):
        A[i].append(cur)
        cur += 1

for i in range(K - 1):
    T = A[i]
    cur = len(T) - 1
    for j in range(cur + 1, K - 1):
        T.append(A[j][cur])
    print(len(T), *T)

T = [A[i][i] for i in range(K - 1)]
print(len(T), *T)