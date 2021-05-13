N = int(input())
A = list(map(int, input().split()))

current = 1000
kabu = 0

for i in range(N-1):
    if A[i] < A[i+1]:
        kabu += current // A[i]
        current = current % A[i]
    elif A[i] > A[i+1]:
        current += kabu * A[i]
        kabu = 0
else:
    current += kabu * A[-1]

print(current)