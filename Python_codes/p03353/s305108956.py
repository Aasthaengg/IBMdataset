S = input()
K = int(input())

A = set()
for i in range(len(S)):
    for j in range(1, min(K + 1, len(S) - i + 1)):
        A.add(S[i:i + j])

A = list(A)
A.sort()
print(A[K - 1])
