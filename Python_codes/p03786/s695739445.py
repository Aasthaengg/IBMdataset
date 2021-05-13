n = int(input())
A = sorted(map(int, input().split()))

t = 0
s = A[0]
for i in range(1, n):
    if 2*s < A[i]:
        t = i
    s += A[i]

print(n-t)