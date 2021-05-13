from collections import Counter
A = list(input())
n = len(A)
b = Counter(A)
z = n * (n - 1) // 2 + 1

for k in b:
    m = b[k]
    z -= m * (m - 1) // 2
print(z)
