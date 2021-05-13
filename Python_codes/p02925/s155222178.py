import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n-1):
        A[i][j] -= 1

AA = [[j for j in i] for i in A]

ID = [[-1] * n for i in range(n)]
id_ = 0
for i in range(n):
    for j in range(i+1,n):
        ID[i][j] = id_
        ID[j][i] = id_
        id_ += 1

for i in range(n):
    for j in range(n-1):
        A[i][j] = ID[i][A[i][j]]

M = [[] for i in range(id_)]
IN = [0] * id_
for i in range(n):
    for j in range(n-2):
        M[A[i][j]].append(A[i][j+1])
        IN[A[i][j+1]] +=1
# print(A)
# print(M)

# 以下、トポロジカルソート

S = []
s = 0

for i in range(id_):
    if IN[i] == 0:
        S.append(i)

while s < len(S):
    for x in M[S[s]]:
        IN[x] -= 1
        # print(x,IN)
        if IN[x] == 0:
            S.append(x)
    s += 1

# print(S)

if len(S) < id_:
    print(-1)
else:
    T = [1] * id_
    for i in range(id_):
        for j in M[S[i]]:
            T[j] = max(T[j], T[S[i]] + 1)
    print(max(T))


# 以下、閉路検出(今は削除)

# V = [0] * id_
# S = [0]
# V[0] = 1

# import sys

# def visit(x):
#     if V[x] == 1:
#         print(-1)
#         sys.exit()
#     elif V[x] == 0:
#         V[x] = 1
#         for i in M[x]:
#             visit(i)
#         V[x] = 2

# for i in range(id_):
#     if V[i] == 0:
#         visit(i)
# print("heironasi")

# 閉路検出ここまで
