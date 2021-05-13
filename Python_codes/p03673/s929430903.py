from collections import deque

N = int(input())
A = list(map(int, input().split()))

res = deque()
for i in range(0, N-1, 2):
    res.append(A[i])
    res.appendleft(A[i+1])

if N % 2 == 1:
    res.append(A[N-1])
    print(" ".join(reversed([str(s) for s in res])))
else:
    print(" ".join(str(s) for s in res))