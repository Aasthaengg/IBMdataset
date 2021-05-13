N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

newA = sorted(A)
ma = newA[N-1]
for i in range(N):
    if A[i] == ma:
        print(newA[N-2])
    else:
        print(ma)