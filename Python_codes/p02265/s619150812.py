from collections import deque

n = int(input())

dlist = deque()

for i in range(n):
    arr = input().split()
    cmd = ''
    key = 0
    cmd = arr[0]
    if len(arr) > 1:
        key = arr[1]
    if cmd == 'insert':
        dlist.appendleft(key)
    elif cmd == 'delete':
        try:
            dlist.remove(key)
        except:
            continue
    elif cmd == 'deleteFirst':
        dlist.popleft()
    elif cmd == 'deleteLast':
        dlist.pop()

print(' '.join(dlist))


