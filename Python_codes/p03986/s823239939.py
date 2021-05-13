from collections import deque
s=input()

A=deque([])
for i in s:
    if len(A)<1:
        A.append(i)
    else:
        if A[-1]+i=="ST":A.pop()
        else:A.append(i)

print(len(A))