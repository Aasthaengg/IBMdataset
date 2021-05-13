h, w, d = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

L = [[0, 0] for _ in range(h*w)]
for i in range(h):
    for j in range(w):
        id = A[i][j]
        id -= 1
        L[id][0] = i
        L[id][1] = j

C = [0]*(h*w)
for i in range(h*w):
    ni = i+d
    if ni <= h*w-1:
        C[ni] = C[i]+abs(L[ni][0]-L[i][0])+abs(L[ni][1]-L[i][1])
#print(C)

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    l, r = l-1, r-1
    print(C[r]-C[l])
