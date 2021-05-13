from collections import deque
N = int(input())
A = deque(sorted(list(map(int, input().split()))))
MAX, MIN = A.pop(), A.popleft()

ans = []
while len(A):
    if A[0] < 0:
        x, y = MAX, A.popleft()
        ans.append([MAX, y])
        MAX = MAX - y
    else:
        x, y = MIN, A.popleft()
        ans.append([x, y])
        MIN = MIN - y

ans.append([MAX, MIN])
print(MAX - MIN)
for x, y in ans:
    print(x, y)
