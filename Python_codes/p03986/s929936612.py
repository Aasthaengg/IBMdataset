# coding: utf-8
from collections import deque
s=input()
n=len(s)
A=deque()
for i in range(n):
    if s[i]=="S":
        A.append(s[i])
    else:
        if len(A)==0:
            A.append(s[i])
        elif A[-1]=="S":
            A.pop()
        else:
            A.append(s[i])
print(len(A))