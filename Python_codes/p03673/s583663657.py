from collections import deque
n = int(input())
a = list(map(str, input().split()))
b = deque([])
t = 1
for i in a:
    if t == -1:
        b.appendleft(i)
    else :
        b.append(i)
    t *= -1
if t == -1:
    b.reverse()
print(*b)