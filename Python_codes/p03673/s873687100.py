from collections import deque

n = int(input())
a = list(map(int, input().split()))

b = deque()

for i in range(n):
    if i % 2 == n % 2:
        b.append(a[i])
    else:
        b.appendleft(a[i])

b = [str(x) for x in b]
print(" ".join(b))
