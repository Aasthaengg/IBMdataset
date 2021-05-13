from collections import deque


B = deque()
n = int(input())
A = list(map(int, input().split()))

for i, a in enumerate(A):
    if i % 2 == 0:
        B.append(a)
    else:
        B.appendleft(a)

if n % 2 == 1:
    B.reverse()
print(*B)
