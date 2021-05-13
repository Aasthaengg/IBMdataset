N = int(input())
S = [list(input()) for i in range(N)]

A = []
B = []

for i in range(N):
    a = 0  # (の個数
    b = 0  # )の個数
    c = 0  # 始点に対する最下点の高さ（(を+1,)を-1とみなす）
    for j in range(len(S[i])):
        if S[i][j] == '(':
            a += 1
        else:
            b += 1
            c = min(a-b,c)
    if a-b >= 0:
        A.append((a-b,c))  # (何個高くなるか,最下点の相対的高さ)
    else:
        B.append((a-b,c))  # (何個高くなるか,最下点の相対的高さ)

a,b = len(A),len(B)

from operator import itemgetter

A = sorted(A,key=itemgetter(1),reverse=True)

c = 0  # Aの元を全て繋げた時,何個高くなるか

for i in range(a):
    if c + A[i][1] < 0:
        print('No')
        exit()
    else:
        c += A[i][0]

for i in range(b):
    B[i] = (-B[i][0],B[i][1]-B[i][0])

B = sorted(B,key=itemgetter(1),reverse=True)

d = 0  # Bの元を全て繋げた時,何個高くなるか

for i in range(b):
    if d + B[i][1] < 0:
        print('No')
        exit()
    else:
        d += B[i][0]

if c == d:
    print('Yes')
else:
    print('No')