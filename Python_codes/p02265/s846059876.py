#coding:utf-8
#1_3_C
from collections import deque
n = int(input())
ary = deque()
for i in range(n):
    cmd = input().split()
    if cmd[0] == "insert":
        ary.appendleft(cmd[1])
    elif cmd[0] == "delete":
        try:
            ary.remove(cmd[1])
        except ValueError:
            pass
    elif cmd[0] == "deleteFirst":
        ary.popleft()
    elif cmd[0] == "deleteLast":
        ary.pop()

print(" ".join(ary))