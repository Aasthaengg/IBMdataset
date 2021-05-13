from collections import deque

N, K = map(int, input().split())
S = input()

q = deque()

cnt = 0
for i in range(N - 1):
    cnt += 1
    if S[i] != S[i + 1]:
        q.append(cnt)
        cnt = 0

q.append(cnt + 1)

for _ in range(K):
    if not q:
        break
    a = q.popleft()
    b = q.popleft() if q else 0
    c = q.popleft() if q else 0
    q.appendleft(a+b+c)

print(sum(q) - len(q))