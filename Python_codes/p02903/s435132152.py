H,W,A,B = map(int,input().split())
C = [["0" for _ in range(W)] for _ in range(H)]
for i in range(H-B):
    for j in range(A,W):
        C[i][j] = "1"
for i in range(H-B,H):
    for j in range(A):
        C[i][j] = "1"
for i in range(H):
    print("".join(C[i]))