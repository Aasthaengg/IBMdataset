S = input()
if S == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()

A = list("abcdefghijklmnopqrstuvwxyz")
if len(S) < 26:
    for i in A:
        if i not in S:
            print(S+i)
            exit()

for i in range(24,0,-1):
    if S[i] != max(S[i:]):
        B = [j for j in S[i+1:] if j > S[i]]
        print(S[:i]+min(B))
        exit()
print(A[A.index(S[0]) + 1])