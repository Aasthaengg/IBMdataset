import collections


Q = collections.deque()
n = int(input())

for _ in range(n):
    input_value = input().split()
    if input_value[0] == 'insert':
        Q.appendleft(input_value[1])
    elif input_value[0] == 'delete':
        if input_value[1] in Q:
            Q.remove(input_value[1])
    elif input_value[0] == 'deleteFirst':
        Q.popleft()
    elif input_value[0] == 'deleteLast':
        Q.pop()
    else:
        raise Error("illegal state")

print(' '.join(map(str, Q)))

