N = int(input())
A = [int(input()) for _ in range(N)]

MAX_1 = sorted(A)[-1]
MAX_2 = sorted(A)[-2]

for i in range(N):
    if A[i] == MAX_1:
        print(MAX_2)
    else:
        print(MAX_1)
