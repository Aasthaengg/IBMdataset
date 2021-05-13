import sys
input = sys.stdin.readline

#input
N = int(input())
A = str(input())
B = str(input())
C = str(input())

#output
difference = [0] * N
for i in range(N):
    if A[i] == B[i] == C[i]:
        difference[i] = 0
    elif A[i] == B[i] and A[i] != C[i]:
        difference[i] = 1
    elif A[i] == C[i] and A[i] != B[i]:
        difference[i] = 1
    elif B[i] == C[i] and B[i] != A[i]:
        difference[i] = 1
    else:
        difference[i] = 2
print(sum(difference))