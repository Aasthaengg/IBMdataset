from collections import deque

n, q = map(int, input().split())
p_que = deque([])

for _ in range(n):
    name, t = map(str, input().split())
    p_que.append([name, int(t)])

sum_time = 0
while True:
    p = p_que.popleft()
    if p[1] <= q:
        sum_time += p[1]
        print(p[0], sum_time)
    else:
        sum_time += q
        p[1] -= q
        p_que.append(p)
    if len(p_que) == 0:
        break
