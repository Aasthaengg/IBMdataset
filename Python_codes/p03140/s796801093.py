N = int( input() )
A = input()
B = input()
C = input()


ans = 0
for i in range(N):
    if A[i] == B[i] and B[i] != C[i]: ans += 1
    if A[i] != B[i] and B[i] == C[i]: ans += 1
    if A[i] != B[i] and A[i] == C[i]: ans += 1
    if A[i] != B[i] and B[i] != C[i] and C[i] != A[i]: ans += 2

print( ans )