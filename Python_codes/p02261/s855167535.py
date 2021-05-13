N = input()
A = raw_input().split()
B = A[:]
for i in xrange(N):
    for j in xrange(N-1, i, -1):
        if B[j][1] < B[j-1][1]:
            B[j], B[j-1] = B[j-1], B[j]
print ' '.join(B)
print 'Stable'

C = A[:]
for i in xrange(N):
    minj = i
    for j in xrange(i, N):
        if A[j][1] < A[minj][1]:
            minj = j
    A[i], A[minj] = A[minj], A[i]
print ' '.join(A)
s = True
for i in xrange(N):
    for j in xrange(i+1, N):
        if A[i][1] == A[j][1] and C.index(A[i]) > C.index(A[j]):
            s = False
print 'Stable' if s else 'Not stable'