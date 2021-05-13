N,K = map(int, input().split())
A = [int(i) for i in input().split()]
A.sort()

if A[-1] < K:
    print("IMPOSSIBLE")
    exit()

from bisect import bisect_left

flag = False
for i in range(N):
    if A[i] == K:
        flag = True
    
    idx = bisect_left(A, K - A[i])
    if idx < N and i != idx and A[idx] == K - A[i]:
        flag = True

if flag:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')