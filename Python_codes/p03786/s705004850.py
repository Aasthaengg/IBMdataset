import bisect

N = int(input())
A = list(map(int,input().split()))
assert len(A) == N
A.sort()
largest = A[-1]

acum = [0] * N
acum[0] = A[0]
for i in range(1, N):
    acum[i] = A[i] + acum[i-1]


def solve():
    unreachable = None
    for i in range(N-2,-1,-1):
        bi = bisect.bisect(A, 2*A[i])
        if 2*acum[bi-1] < A[i+1]:
            unreachable = i
            break
    if unreachable is None:
        return N
    return N - unreachable - 1


print(solve())