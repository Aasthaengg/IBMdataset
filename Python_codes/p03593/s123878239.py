h, w = map(int,input().split())
AA = [list(input()) for i in range(h)]

import string
A = [chr(i) for i in range(ord("a"), ord("z")+1)]
B = {}
for i in range(26):
    B[A[i]] = i

C = [0, 0, 0]
if h%2 == 1 and w%2 == 1:
    C = [(h-1) * (w-1) // 4, ((h-1) + (w-1)) // 2, 1]
elif h%2 == 1:
    C = [(h-1) * w // 4, w // 2, 0]
elif w%2 == 1:
    C = [(w-1) * h // 4, h // 2, 0]
else:
    C = [h * w // 4, 0, 0]

D = [0] * 26
for i in range(h):
    for j in range(w):
        D[B[AA[i][j]]] += 1

E = [0, 0, 0]
for i in range(26):
    if D[i] % 2 > 0:
        E[2] += 1
    elif D[i] % 4 > 0:
        E[1] += 1

if C[2] == E[2] and C[1] >= E[1]:
    print("Yes")
else:
    print("No")