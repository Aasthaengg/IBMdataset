from collections import deque
n = int(input())
al = list(map(int,input().split()))

b = deque()

if n % 2 == 0:
    for i in range(n):
        if i % 2 != 0:
            b.appendleft(str(al[i]))
        else:
            b.append(str(al[i]))
else:
    for i in range(n):
        if i % 2 == 0:
            b.appendleft(str(al[i]))
        else:
            b.append(str(al[i]))

print(' '.join(b))