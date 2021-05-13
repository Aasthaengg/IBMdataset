from collections import deque

n = int(input())
A = list(map(str, input().split()))

b = deque()
for i in range(n):
    if i % 2 == n % 2:
        b.append(A[i])
    else:
        b.appendleft(A[i])

print(" ".join(list(b)))