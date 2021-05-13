N = int(input())
A = list(map(int, input().split()))

A.sort()
stop = N
for i in reversed(range(N-1)):
    if A[i]* 2 < A[i+1]:
        if 2 * sum(A[:i+1]) < A[i+1]:
            stop = i
            break

print(len(A[stop+1:]) if stop != N else N)
