import collections

N = int(input())
A = list(map(int, input().split()))
ans = collections.deque()
for i in range(N):
    if N % 2 == 0:
        if i % 2 == 0:
            ans.append(A[i])
        else:
            ans.appendleft(A[i])
    else:
        if i % 2 == 0:
            ans.appendleft(A[i])
        else:
            ans.append(A[i])
print(*ans)
