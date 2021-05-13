n = int(input())

A, B = [], []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

s, t = 0, 0
if n % 2 == 0:
    s = (A[n//2-1] + A[n//2])
    t = (B[n//2-1] + B[n//2])
else:
    s = A[n//2]
    t = B[n//2]

print(t-s+1)