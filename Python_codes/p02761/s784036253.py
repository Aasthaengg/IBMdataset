N, M = [int(i) for i in input().split()]
A = []
if N == 1:
    A = [str(i) for i in range(10)]
else:
    A = [str(i) for i in range(10**(N-1), 10**N)]

for i in range(M):
    s, c = [int(j) for j in input().split()]
    A = [a for a in A if a[s-1] == str(c)]
if len(A) > 0:
    print(A[0])
else:
    print(-1)