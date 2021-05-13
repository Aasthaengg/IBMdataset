s = list(input())

A = list(set(s))

B = []

for i in range(len(A)):
    C = []
    for j in range(len(s)):
        if A[i] == s[j]:
            C.append(j)
    C.append(-1)
    C.append(len(s))
    C = sorted(C)
    D = []
    for i in range(len(C) - 1):
        D.append(C[i+1] - C[i] - 1)
    
    B.append(max(D))
print(min(B))