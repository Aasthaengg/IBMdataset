from collections import deque

S = input().split()
dq = deque()

for i in range(len(S)):
    if S[i] == '+':
        a = dq.pop()
        b = dq.pop()
        dq.append(b+a)
    elif S[i] == '-':
        a = dq.pop()
        b = dq.pop()
        dq.append(b-a)
    elif S[i] == '*':
        a = dq.pop()
        b = dq.pop()
        dq.append(b*a)
    else:
        dq.append(int(S[i]))

print(dq[0]) 