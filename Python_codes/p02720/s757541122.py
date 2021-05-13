from queue import deque
k = int(input())
que = deque(range(1,10))

for _ in range(k):
    x = que.popleft()
    if not x % 10 == 0:
        # 123: 10*123 + 123 % 10 = 1233
        que.append(10*x+(x%10)-1)
    que.append(10*x+(x%10))
    if not x %10 == 9:
        que.append(10*x+(x%10)+1)
print(x)