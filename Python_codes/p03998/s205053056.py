from collections import deque
a = list(input())
b = list(input())
c = list(input())

a = deque(a)
b = deque(b)
c = deque(c)

x = 'a'
while True:
    if x == 'a':
        if a:
            x = a.popleft()
        else:
            print('A')
            exit()
    elif x == 'b':
        if b:
            x = b.popleft()
        else:
            print('B')
            exit()
    else:
        if c:
            x = c.popleft()
        else:
            print('C')
            exit()
