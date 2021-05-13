from collections import deque
X = input()
que = deque()
for x in X:
    if x=='S':
        que.append('S')
    elif x=='T' and (not que or que[-1]=='T'):
        que.append('T')
    elif x=='T' and que[-1]=='S':
        _ = que.pop()
print(len(que))