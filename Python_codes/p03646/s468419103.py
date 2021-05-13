K = int(input())

A = [49] * 50
q, r = divmod(K, 50)
for i in range(50):
    A[i] += q
for i in range(r):
    for j in range(50):
        if i == j:
            A[j] += 50
        else:
            A[j] -= 1

print(50)
print(*A)