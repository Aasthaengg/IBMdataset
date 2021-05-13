from collections import deque

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

bc = [list(map(int, input().split())) for _ in range(m)]

a.sort(reverse = False)
bc.sort(key = lambda x: x[1], reverse = True)

q = deque(bc)

s = 0

b, c = q.popleft()

for x in a:
    #print(x, b, c)
    if b == 0:
        if len(q) > 0:
            b, c = q.popleft()
        else:
            b, c = n, 0
    
    if x < c:
        s += c
        b -= 1
    else:
        s += x

print(s)