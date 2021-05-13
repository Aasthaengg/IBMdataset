import sys
C1 = list(input())
C2 = list(input())

if C2 == C1[::-1]:
    print("YES")
else:
    print("NO")