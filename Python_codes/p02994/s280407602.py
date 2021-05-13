N, L = map(int, input().split())
A = [L + i for i in range(N)]
M = L + N - 1
for x in A:
    if abs(M) > abs(x):
        M = x
print(sum(A) - M)
