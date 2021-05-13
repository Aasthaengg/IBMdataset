h, w, d = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

B = [0]*(h*w)

C = [0]*(h*w)

for i in range(h):
    for j in range(w):
        a = A[i][j]
        B[a-1] = (j+1, i+1)

for i in range(h*w):
    if i-d >= 0:
        j = i-d
        px, py = B[j]
        x, y = B[i]
        C[i] = abs(x-px)+abs(y-py)+C[j]
    else:
        C[i] = 0
#print(C)

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    l, r = l-1, r-1
    print(C[r]-C[l])
