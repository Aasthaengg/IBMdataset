n, k = 50, int(input())
A = list(range(n))

q, r = k // n, k % n
A = [a + q for a in A]
for i in range(r):
    A[i] += n + 1
    A = [a - 1 for a in A]

print(n)
print(*A)
