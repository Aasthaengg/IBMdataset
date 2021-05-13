from collections import deque
k = int(input())
l = deque([i for i in range(1, 10)])
# print(l)

for i in range(k):
    x = l.popleft()
    mod = x % 10
    if mod != 0:
        l.append(x*10 + mod - 1)
    l.append(x*10 + mod)
    if mod != 9:
        l.append(x*10 + mod + 1)

print(x)