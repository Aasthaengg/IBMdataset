N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

B = A.copy()
B.sort(reverse=True)
for i in range(N):
    if A[i] != B[0]:
        print(B[0])
    else:
        print(B[1])

