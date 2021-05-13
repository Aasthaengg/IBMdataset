from collections import deque

s = input()
s2 = s.replace('x', '')
if s2 != s2[::-1]:
    print(-1)
else:
    d = deque(s)
    a, b = [], []
    cnt = 0
    x = y = ''
    x_skip = y_skip = 0
    while d:
        if not x_skip:
            x = d.popleft()
        if 0 < len(d)and not y_skip:
            y = d.pop()

        if y == '':
            break

        if x == y != 'x':
            cnt += abs(len(a)-len(b))
            x = y = ''
            a, b = [], []
            x_skip = y_skip = 0
            continue

        if x == 'x':
            a.append(x)
        else:
            x_skip = 1

        if y == 'x':
            b.append('x')
        else:
            y_skip = 1
    else:
        cnt += abs(len(a)-len(b))

    print(cnt)