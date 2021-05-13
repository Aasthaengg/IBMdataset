from collections import deque
A = deque(map(str, input()))
B = deque(map(str, input()))
C = deque(map(str, input()))
x = A.popleft()
for _ in range(10000000):
    if x == "a":
        if A:
            x = A.popleft()
        else:
            print("A")
            break
    elif x == "b":
        if B:
            x = B.popleft()
        else:
            print("B")
            break
    else:
        if C:
            x = C.popleft()
        else:
            print("C")
            break