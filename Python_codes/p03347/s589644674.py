N = int(input())
A = [-1] + [int(input()) for _ in range(N)]

count = -1
for i in range(N, 0, -1):
    if A[i] - 1 > A[i - 1]:
        print (-1)
        exit()
    elif A[i] - 1 == A[i - 1]:
        count += 1
    else:
        count += A[i]

print (count)