import sys
import collections
n = int(input())
que = collections.deque()

for _ in range(n):
    command = sys.stdin.readline()
    if 'i' == command[0]:
        command, num = command.split()
        que.appendleft(num)
    elif 'deleteFirst\n' == command:
        que.popleft()
    elif 'deleteLast\n' == command:
        que.pop()
    else:
        command, num = command.split()
        try:
            que.remove(num)
        except ValueError:
            pass
print(' '.join(map(str, que)))