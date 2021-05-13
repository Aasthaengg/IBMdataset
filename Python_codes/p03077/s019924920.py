N = int(input())
A = []
for a in range(5):
    b = int(input())
    A.append(b)

A.sort()
if A[0] >= N:
    print(5)
    exit()
else:
    if N % A[0] == 0:
        print(N // A[0] + 4)
        exit()
    else:
        print(N // A[0] + 5)
        exit()