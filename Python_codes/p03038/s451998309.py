N, M = [int(x) for x in input().split()]
A = sorted([int(x) for x in input().split()])

data = []
for i in range(M):
    B, C = [int(x) for x in input().split()]
    data.append([C, B])
data = sorted(data, reverse=True)

D = []
i, tot = 0, 0
while tot < N and i < M:
    C, B = data[i][0], data[i][1]
    for _ in range(B):
        D.append(C)
        tot += 1
        if tot >= N:
            break
    i += 1

i = 0
while i < min(N, len(D)) and A[i] < D[i]:
    i += 1

ans = sum(D[:i] + A[i:])
print(ans)