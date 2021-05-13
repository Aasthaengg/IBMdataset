from collections import deque
sa = deque(input())
sb = deque(input())
sc = deque(input())

player = "a"
while True:
    if player == "a":
        if len(sa) == 0:
            print("A")
            break
        player = sa.popleft()
    elif player == "b":
        if len(sb) == 0:
            print("B")
            break
        player = sb.popleft()
    else:
        if len(sc) == 0:
            print("C")
            break
        player = sc.popleft()