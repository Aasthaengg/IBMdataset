K = int(input())
q = K // 50
r = K % 50
A = list(range(q, 50 + q))

for i in range(r):
    A[i] += 51 - r
for i in range(r, 50):
    A[i] -= r
print(50)
print(*A)