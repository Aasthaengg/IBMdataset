H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))
B = []
for i, a in enumerate(A):
    B.append((a, i+1))

A = sorted(B)
i, j = 0, 0
C = [[0]*W for _ in range(H)]
flag = True
for k in range(N):
    num, color = A[k]
    while num:
        C[i][j] = color
        if flag:
            if j < W-1:
                j += 1
            else:
                i += 1
                flag = False
        else:
            if j > 0:
                j -= 1
            else:
                i += 1
                flag = True
        num -= 1

for k in range(H):
    print(*C[k])

