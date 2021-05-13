from collections import deque

N = int(input())
A = deque(maxlen=N)
x = [int(e) for e in input().split()]
x.sort()
for a in x:
    A.append(a)
l = []
for i in range(N - 2):
    (a, b, c) = (A[0], A[1], A[-1])
    if b < 0:
        l.append((c, a))
        A[-1] = c - a
    else:
        l.append((a, b))
        A[1] = a - b
    A.popleft()
print(A[1] - A[0])
l.append((A[1], A[0]))
for v in l:
    print(v[0], v[1])