A, B, K = map(int, input().split())

a = min(A, K)
A -= a
K -= a
b = min(B, K)
B -= b
print(str(A) + " " + str(B))