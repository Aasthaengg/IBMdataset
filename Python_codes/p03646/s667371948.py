N = 50
A = [i for i in range(N)]
K = int(input())
a = K//N
k = K%N
A = [A[i]+a for i in range(N)]
for _ in range(k):
    amin = 10**17
    for i in range(N):
        if A[i]<amin:
            ind = i
            amin = A[i]
    for i in range(N):
        if i==ind:
            A[i] += N
        else:
            A[i] -= 1
print(N)
print(*A)