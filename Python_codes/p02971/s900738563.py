N = int(input())
A = []
max1 = 0
max2 = 0

for _ in range(N):
    tmp = int(input())
    A.append(tmp)
    if tmp > max1:
        max1 = tmp
    elif tmp > max2:
        max2 = tmp

for i in range(N):
    if A[i] == max1:
        print(max2)
    else:
        print(max1)
