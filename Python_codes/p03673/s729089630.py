from collections import deque

n = int(input())
a = list(map(int, input().split()))

b = deque([])

if n % 2 == 0:
    flag = True
else:
    flag = False

for i in range(n):
    if flag:
        b.append(a[i])
        flag = not flag
    else:
        b.appendleft(a[i])
        flag = not flag

print(' '.join(map(str, b)))