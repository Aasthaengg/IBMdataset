import collections

N = int(input())
A = [int(input()) for _ in range(N)]

A = dict(collections.Counter(A))

cnt = 0
for a in A:
    if A[a] % 2 == 1:
        cnt += 1
        
print(cnt)