import collections

n = int(input())
que = collections.deque()

for i in range(n):
    line = input()

    if line[0] == 'i':
        que.appendleft(int(line[7:]))
    elif line[6] == ' ':
        try:
            que.remove(int(line[7:]))
        except ValueError:
            pass
    elif line[6] == 'F':
        que.popleft()
    else:
        que.pop()

print(*que)

