import numpy as np
N, M = map(int, input().split())
H = list(map(int, input().split()))
A = list(map(int, input().split()) for _ in range(M))
A = list(map(list, set(map(tuple, A))))
#print(A)
#1本の道を辿っていける展望台の標高の最大値を求める
h = np.ones((N))

ans = 0
tmp = 0
for i in range(len(A)):
    if H[A[i][0]-1] > H[A[i][1]-1]:
        h[A[i][1]-1] = 0
    elif H[A[i][0]-1] < H[A[i][1]-1]:
        h[A[i][0]-1] = 0
    elif H[A[i][0]-1] == H[A[i][1]-1]:
        h[A[i][0]-1] = 0
        h[A[i][1]-1] = 0
#print(h)       
for i in range(N):
    if h[i]==1:
        ans+=1
print(ans)