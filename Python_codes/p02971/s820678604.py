N = int(input())
A = []
for n in range(N):
    A.append(int(input()))

B = sorted(A, reverse = True)
max1 = B[0]
max2 = B[1]
for a in A:
    print(max2 if a == max1 else max1)