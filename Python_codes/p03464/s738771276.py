import math

K = int(input())

A = input().split()

for i in range(K):
    A[i] = int(A[i])

maxlst = [0 for i in range(K)]
minlst = [0 for i in range(K)]

if A[K-1] != 2:
    print(-1)
    quit()

maxlst[K-1] = 3
minlst[K-1] = 2

for i in reversed(range(K-1)):
    if maxlst[i+1] < A[i] or (maxlst[i+1] % A[i] != 0 and minlst[i+1] % A[i] != 0 and int(maxlst[i+1]/A[i]) == int(minlst[i+1]/A[i])):
        print(-1)
        quit()
    maxlst[i] = int(A[i] - 1 + A[i] * math.floor(maxlst[i+1] / A[i]))
    minlst[i] = int(math.ceil(minlst[i+1] / A[i]) * A[i])

print(minlst[0], maxlst[0])
