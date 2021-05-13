import sys
input = sys.stdin.readline

A,B,C = input().split()
A=list(A)
B=list(B)
C=list(C)

if A[-1]==B[0] and B[-1]==C[0]:
    print("YES")
else:
    print("NO") 

