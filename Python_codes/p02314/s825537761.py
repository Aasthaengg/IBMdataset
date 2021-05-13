N, M = map(int, input().split())
C = [int(x) for x in input().split()]
C.sort()
A = [0 for _ in range(N + 1)]
for c in C:
    if c > N:
        break
    A[c] = 1
for i in range(1, N + 1):
    pos = []
    for c in C:
        if i - c < 0:
            break
        pos.append(A[i - c])
    A[i] = min(pos) + 1
print(A[-1])

