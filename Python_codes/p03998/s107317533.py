from collections import deque
a = deque(input())
a.append("a")
b = deque(input())
b.append("b")
c = deque(input())
c.append("c")
 
start = a.popleft()
while a and b and c:
    if start == "a":
        start = a.popleft()
    elif start == "b":
        start = b.popleft()
    else:
        start = c.popleft()
 
print(str(start).upper())