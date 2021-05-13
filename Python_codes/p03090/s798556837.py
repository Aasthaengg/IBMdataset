N = int(input())

M = N - 1 if N % 2 == 1 else N

A = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i < j and j != M:
            A.append((i, j))
    M -= 1

print(len(A))
for a in A:
    print(*a)