N, M = map(int, input().split())
B = []
for _ in range(M):
    a, b = map(int, input().split())
    B.append([b, a])
B.sort()
C = []
i = 0
while True:
    C.append(B[i])
    if i == M - 1:
        break
    j = 1
    while True:
        if B[i][0] > B[i + j][1]:
            j += 1
            if i + j == M:
                break
            continue
        else:
            break
    if i + j == M:
        break
    i = i + j
print(len(C))