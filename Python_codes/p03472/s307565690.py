from collections import deque
N, H = map(int, input().split())
a, b = [], []
for _ in range(N):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
a.sort()
b.sort()
maxa = a[-1]
que = deque(b)
cnt = 0
while H > 0:
    if not que:
        cnt += -(-H//maxa)
        break
    maxb = que.pop()
    if maxb > maxa:
        cnt += 1
        H -= maxb
    else:
        cnt += -(-H//maxa)
        break
print(cnt)