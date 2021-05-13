import math
K = int(input())
A = list(map(int, input().split()))
N_min = 2
N_max = 2

for i in range(K-1,-1,-1):
    N_max = int(math.floor(N_max/A[i]))*A[i] + A[i]-1
    N_min = int(math.ceil(N_min/A[i]))*A[i]
    if N_max < A[i]:
        print(-1)
        exit()
    if N_max < N_min:
        print(-1)
        exit()

print(N_min,N_max)
