import sys

n = int(raw_input())
A = map(int, sys.stdin.readline().split())

cnt = 0

for i in xrange(len(A)-1):
    for j in xrange(len(A)-1, i, -1):
        if A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            cnt += 1

for x in A:
	print x,
print 
print cnt