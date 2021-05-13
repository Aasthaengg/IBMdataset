from collections import deque
N = int(input())
A = [int(a) for a in input().split()]

q = deque()
for i in range(N):
    if i%2 == 0:
        q.append(A[i])
    else:
        q.appendleft(A[i])

ans = list(q)
if N%2 == 1:
    ans.reverse()
print(*ans)