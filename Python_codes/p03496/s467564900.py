N = int(input())
A = list(map(int, input().split()))
K = 0
t = 0
place = 0
for i in range(N):
    if abs(A[i]) > K:
        K = abs(A[i])
        place = i
        if A[i] >= 0:
            t = 0
        else:
            t = 1
print(2*N-2)
if t == 0:
    print(place+1, 2)
    print(place+1, 2)
    for i in range(2, N):
        print(i, i+1)
        print(i, i+1)
else:
    print(place+1, N-1)
    print(place+1, N-1)
    for i in range(N-2, 0, -1):
        print(i+1, i)
        print(i+1, i)