N, K = map(int, input().split())
A = list(map(int, input().split()))

A = list(set(A))
N = len(A)
A.sort()

if K > max(A):
    print("IMPOSSIBLE")
    exit()

if N == 1:
    if A[0] == K:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
    exit()

min_diff = min([A[i] - A[i-1] for i in range(1,N)])

for i in range(N):
    if abs(A[i]-K) % min_diff == 0:
        print("POSSIBLE")
        break
else:
    print("IMPOSSIBLE")