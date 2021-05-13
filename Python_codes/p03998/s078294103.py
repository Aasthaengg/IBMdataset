from collections import deque
sa = deque(list(input()))
sb = deque(list(input()))
sc = deque(list(input()))

flag = True
next = sa
while flag:
    x = next.popleft()
    if x =='a':
        if not sa:
            print('A')
            break
        next = sa
    elif x =='b':
        if not sb:
            print('B')
            break
        next = sb
    else:
        if not sc:
            print('C')
            break
        next = sc