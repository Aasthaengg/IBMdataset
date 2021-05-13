from collections import deque
a = deque(input())
b = deque(input())
c = deque(input())

i = 0
turn = 'a'
while True:
    if turn == 'a':
        if len(a) == 0:
            ans = 'A'
            break
        a0 = a.popleft()
        if a0 == 'a':
            turn = 'a'
        elif a0 == 'b':
            turn = 'b'
        elif a0 == 'c':
            turn = 'c'
    elif turn == 'b':
        if len(b) == 0:
            ans = 'B'
            break
        b0 = b.popleft()
        if b0 == 'a':
            turn = 'a'
        elif b0 == 'b':
            turn = 'b'
        elif b0 == 'c':
            turn = 'c'
    elif turn == 'c':
        if len(c) == 0:
            ans = 'C'
            break
        c0 = c.popleft()
        if c0 == 'a':
            turn = 'a'
        elif c0 == 'b':
            turn = 'b'
        elif c0 == 'c':
            turn = 'c'
print(ans)