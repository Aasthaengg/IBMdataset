a, b = map(int,input().split())
A = [[0]*b for i in range(a)]
B = [0] * b

for i in range(a):
    A[i] = list(map(int,input().split()))

for i in range(b):
    B[i] = int(input())

for i in range(a):
    s=0
    for j in range(b):
        s+=A[i][j]*B[j]
    print(s)