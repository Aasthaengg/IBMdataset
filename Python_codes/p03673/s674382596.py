from collections import deque 
n = int(input())

a = list(input().split())
b = []

q = deque()

for i in range(n):
    x = a[i]
    if n%2 == i%2:
        q.append(x)
    else:
        q.appendleft(x)

    
print(" ".join(q))    