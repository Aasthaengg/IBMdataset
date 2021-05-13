k, t = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

C = []
for i in range(t):
    C += [i]*A[i]

from collections import deque
B = deque(C)
L = [-1]*k
for i in range(k):
    if i%2 == 0:
        L[i] = B.popleft()
    else:
        L[i] = B.pop()

ans1 = 0
for i in range(1, k):
    if L[i-1] == L[i]:
        ans1 += 1

B = deque(C)
L = [-1]*k
for i in range(k):
    if i%2 == 0:
        L[i] = B.pop()
    else:
        L[i] = B.popleft()

ans2 = 0
for i in range(1, k):
    if L[i-1] == L[i]:
        ans2 += 1

print(min(ans1, ans2))
