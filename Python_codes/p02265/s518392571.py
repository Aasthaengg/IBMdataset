from collections import deque

n = int(input())

commnad = ''
key = 0
dll = deque()
cur = 0

for i in range(n):
    tmp = input()
    if ' ' in tmp:
        command, key = tmp.split(' ')
    else:
        command = tmp

    if command == 'insert':
        dll.appendleft(key)
    elif command == 'delete':
        try:
            dll.remove(key)
        except:
            pass
    elif command == 'deleteFirst':
        dll.popleft()
    elif command == 'deleteLast':
        dll.pop()

res = ''
for i in dll:
    res += i
    res += ' '
print(res[:-1])
