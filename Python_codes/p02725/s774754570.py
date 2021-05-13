import sys
 
read = sys.stdin.buffer.read
K,N,*A = map(int, read().split())
A += [A[0]+K]
gap = max(y-x for x,y in zip(A, A[1:]))
 
print(K-gap)