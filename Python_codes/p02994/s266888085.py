N,L = [int(i) for i in input().split()]

A = [i+L-1 for i in range(1,N+1)]
B = [abs(i+L-1) for i in range(1,N+1)]

print(sum(A)-A[B.index(min(B))])
