n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

T = [[0]*2001 for i in range(n)]

T[0][0] = 1
T[0][A[0]] = 1
for i in range(1,n):
    for j in range(2001):
        T[i][j] = T[i-1][j]
        if (j - A[i] >=0) and (T[i-1][j-A[i]] == 1):
            T[i][j] = 1
    
for i in range(m):
    if T[n-1][B[i]] == 1:
        print("yes")
    else:
        print("no")

