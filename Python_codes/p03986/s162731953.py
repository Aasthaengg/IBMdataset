from collections import deque

s = input()
n = len(s)
que = deque()
for i in range(n):
    if s[i] == 'S':
        que.append(s[i])
    else:
        if len(que) == 0:
            que.append(s[i])
        elif que[-1] == 'T':
            que.append(s[i])
        else:
            que.pop()
    
print(len(que))