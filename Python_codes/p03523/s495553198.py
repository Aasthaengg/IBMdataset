S = list(input())
A = list("AKIHABARA")
B = list("AKIHABARA")
j = 0
for i in range(9):
    if j == len(S):
        A[i] = "A"
    elif S[j] == A[i]:
        j += 1
    else:
        A[i] = "A"

if A == B and j == len(S):
    ans = "YES"
else:
    ans = "NO"
print(ans)
