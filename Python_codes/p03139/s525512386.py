import sys
input = sys.stdin.readline

#input
N, A, B = map(int, input().split())

#output
M = min(A, B)
m = 0
if A+B > N:
    m = A+B-N
else:
    m = 0

print(M, m, sep = " ")