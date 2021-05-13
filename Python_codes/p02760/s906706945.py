A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

N = int(input())
B = set()
for _ in range(N):
    B.add(int(input()))

for i in range(3):
    for j in range(3):
        if A[i][j] in B:
            A[i][j] = -1

Q = [-1,-1,-1]
for i in range(3):
    if A[i] == Q:
        print("Yes")
        exit()
A = list(zip(*A))
Q = (-1,-1,-1)
for i in range(3):
    if A[i] == Q:
        print("Yes")
        exit()

if A[0][0] == A[1][1] == A[2][2] or A[0][2] == A[1][1] == A[2][0]:
    print("Yes")
    exit()

print("No")
