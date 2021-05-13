from collections import deque
a = int(input())

dl = deque()
for i in range(a):
    o = input().split()

    if o[0] == 'delete':
        try:
            dl.remove(o[1])
        except ValueError:
            pass
    elif o[0] == 'deleteFirst':
        dl.popleft()
    elif o[0] == 'deleteLast':
        dl.pop()
    else:
        dl.appendleft(o[1])

print(" ".join([str(i) for i in dl]))

