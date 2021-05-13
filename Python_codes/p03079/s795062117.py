from sys import stdin

A, B, C = stdin.readline().rstrip().split() 
if A == B and B == C and C == A:
    print("Yes")
else:
    print("No")