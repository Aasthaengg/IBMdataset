n = int(input())
A = [int(i) for i in input().split()]

C = []
max_A = max(A)
max_idx = A.index(max_A)
min_A = min(A)
min_idx = A.index(min_A)

if abs(max_A) >= abs(min_A):
    for i in range(n):
        #A[i] += max_A
        C.append([max_idx+1, i+1])
    for i in range(1, n):
        #A[i] += A[i-1]
        C.append([i, i+1])
else:
    for i in range(n):
        #A[i] += min_A
        C.append([min_idx+1, i+1])
    for i in range(n, 1, -1):
        #A[n-i+2] += A[n-i+1]
        #C.append([n-i+2, n-i+3])
        C.append([i, i-1])

print(len(C))
for i, j in C:
    print('{0} {1}'.format(i, j))
