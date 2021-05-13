n = raw_input()
A = map(int, raw_input().split())
cnt = 0
for i in xrange(len(A)):
    mini = i
    for j in xrange(i, len(A)):
        if A[j] < A[mini]:
            mini = j
    if A[i]!=A[mini]:
	    cnt += 1
	    A[i], A[mini] = A[mini], A[i]
for x in A:
	print x,
print
print cnt