N = int(input())
XL = [list(map(int, input().split())) for _ in range(N)]
A = []
for x, l in XL:
    A.append([x + l, x - l])
A.sort()
B = []
i = 0
while True:
    B.append(A[i])
    if i == N - 1:
        break
    j = 1
    while True:
        if A[i][0] > A[i + j][1]:
            j += 1
            if i + j == N:
                break
            continue
        else:
            break
    if i + j == N:
        break
    i = i + j
print(len(B))