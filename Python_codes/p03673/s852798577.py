from collections import deque

n = int(input())
a = input().split()
d = deque([])
for i in range(n):
    if i % 2 == 0:
        d.append(a[i])  # 右に足す
    else:
        d.appendleft(a[i])  # 左に足す
if (n % 2) == 1:
    print(' '.join(list(d)[::-1]))
else:
    print(' '.join(list(d)))
