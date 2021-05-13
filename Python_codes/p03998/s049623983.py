from collections import deque
sa = deque(str(input()))
sb = deque(str(input()))
sc = deque(str(input()))
p = sa.popleft()
while 1:
    if p =="a":
        if len(sa) == 0:
            print("A")
            exit()
        p = sa.popleft()
       
    elif p == "b":
        if len(sb) == 0:
            print("B")
            exit()
        p = sb.popleft()
    else:
        if len(sc) == 0:
            print("C")
            exit()
        p = sc.popleft()
