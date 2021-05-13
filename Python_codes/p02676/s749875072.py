K = int(input())
S = input()
if K < len(S):
    A = ""
    for i in range(K):
        A = str(A) + S[i]
    A = str(A) + "..."
    S = A
print(S)