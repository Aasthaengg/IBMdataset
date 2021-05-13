def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

from collections import deque
n = INT()
a = LI()
b = deque()

for i in range(n):
    if i % 2 == 0:
        b.append(a[i])
    else:
        b.appendleft(a[i])
        
if (-1)**n == -1:
    b.reverse()
    
print(*b)