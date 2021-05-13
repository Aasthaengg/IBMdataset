A, B, C = input().split()
res = "NO"
if A[-1] == B[0] and B[-1] == C[0]:
    res = "YES"

print(res)