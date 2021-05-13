N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
A.insert(N+1, 0)
total = 0
for i in range(N+1):
    total += abs(A[i+1] - A[i])
for j in range(1, N+1):
    print(total + abs(A[j + 1] - A[j - 1]) - abs(A[j + 1] - A[j]) - abs(A[j-1] - A[j]))