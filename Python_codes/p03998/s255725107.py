from collections import deque
Sa = input()
Sb = input()
Sc = input()
a = deque(list(Sa))
b = deque(list(Sb))
c = deque(list(Sc))

x = 'a'
while True:
    if x == 'a':
        if not a:break
        x = a.popleft()
    elif x == 'b':
        if not b:break
        x = b.popleft()
    elif x == 'c':
        if not c:break
        x = c.popleft()
if x == 'a':
    print('A')
elif x == 'b':
    print('B')
else:
    print('C')