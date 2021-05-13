def exe():
    print('Yes')
    exit()

A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

N = int(input())
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                A[i][j] = 0

for i in range(3):
    if sum(A[i]) == 0:
        exe()
    elif A[0][i]+A[1][i]+A[2][i]==0:
        exe()
if A[0][0]+A[1][1]+A[2][2] == 0:
    exe()
elif A[0][2]+A[1][1]+A[2][0] == 0:
    exe()

print('No')