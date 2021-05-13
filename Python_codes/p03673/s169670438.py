# C - pushpush
# https://atcoder.jp/contests/abc066/tasks/arc077_a

from collections import deque

n = int(input())
a = input().split()

b = deque(maxlen=n)

for i in range(n):
    if n%2 == 0: 
        if i%2 == 0:
            b.append(a[i])
        else:
            b.appendleft(a[i])
    else:
        if i%2 == 0:
            b.appendleft(a[i])
        else:
            b.append(a[i])
print(*b)