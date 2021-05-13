n = int(input())
A = [int(x) for x in range(1,34000)]
for i in range(33999):
    A[i] = A[i]**2

B = [i for i in A if i <= n]

print(max(B))