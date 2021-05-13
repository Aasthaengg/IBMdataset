h, w, a, b = map(int,input().split())
A = [[0] * w for i in range(h)]
for i in range(h):
    for j in range(w):
        A[i][j] = int((j < a) ^ (i < b))

for i in range(h):
    print("".join([str(j) for j in A[i]]))