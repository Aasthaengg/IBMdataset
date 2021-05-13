A,B,C = map(str, input().split())

A_last = (A[-1])
B_first = (B[0]) 
B_last = (B[-1])
C_first = (C[0])

if A_last == B_first and B_last == C_first:
    print("YES")
else:
    print("NO")