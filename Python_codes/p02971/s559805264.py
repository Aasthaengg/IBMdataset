N = int(input())

A = [int(input()) for _ in range(N)]

max1 = max(A)
max1_ind = A.index(max1)

A.remove(max1)

max2 = max(A)

for i in range(N):
    if i != max1_ind:
        print(max1)
    else:
        print(max2)

