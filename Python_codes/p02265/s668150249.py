# -*- coding:utf-8 -*-
import collections
n = int(input())
ans = collections.deque()

for i in range(n):
    command = input().split()
    if command[0] == "insert":
        ans.appendleft(command[1])
    elif ans == []:
        continue
    elif command[0] == "delete":
        try:
            ans.remove(command[1])
        except:
            pass
    elif command[0] == "deleteFirst":
        ans.popleft()
    else:
        ans.pop()

print (' '.join(ans))