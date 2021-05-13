N = int(input())

from collections import deque

q = deque()

q.append('a')

while True:
    str = q.popleft()
    temp_lst = list(str) + [chr(ord('a') + len(set(str)))]
    temp_lst = list(set(temp_lst))
    temp_lst.sort()
    for c in temp_lst:
        q.append(str + c)
    if len(str) < N:
        continue
    elif len(str) == N:
        print(str)
    else:
        break