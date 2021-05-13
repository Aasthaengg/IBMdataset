from collections import deque

N = int(input())
t = deque([0] * N)
x = deque([0] * N)
y = deque([0] * N)

for i in range(N):
    t[i], x[i], y[i] = map(int, input().split())

N += 1
t.appendleft(0)
x.appendleft(0)
y.appendleft(0)

for i in range(N-1):
    t_sub = t[i+1] - t[i]
    x_sub = abs(x[i+1] - x[i])
    y_sub = abs(y[i+1] - y[i])
    dist = x_sub + y_sub
    if dist > t_sub or t_sub % 2 != dist % 2:
        print('No')
        exit()

print('Yes')