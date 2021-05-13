N = int(input())
A = sorted(map(int, input().split()))
d = 0
for i in range(1, N):
    d += A[i] - A[i-1]
print(d)
