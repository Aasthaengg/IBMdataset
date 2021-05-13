N = int(input())
A = [0] * N 
for i in range(N):
    A[i] = int(input())

B = sorted(A)
max1 = B[-1]
max2 = B[-2]
for x in A:
    if x == max1:
        print(max2)
    else:
        print(max1)