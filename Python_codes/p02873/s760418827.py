S = input()
A = [0 for _ in range(len(S) + 1)]

for idx in range(len(S)):
    if S[idx] == "<":
        A[idx + 1] = max(A[idx + 1], A[idx] + 1)

for idx in reversed(range(len(S))):
    if S[idx] == ">":
        A[idx] = max(A[idx], A[idx + 1] + 1)

print(sum(A))
