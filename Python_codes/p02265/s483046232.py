# -*- coding: utf-8 -*-

from collections import deque

COMMAND = ("insert", "delete", "deleteFirst", "deleteLast")

if __name__ == "__main__":
    n = int(input())
    ans = deque()
    for i in range(n):
        com = input().split()
        if com[0] == COMMAND[0]:
            ans.appendleft(com[1])
        elif com[0] == COMMAND[1]:
            if com[1] in ans:
                ans.remove(com[1])
        elif com[0] == COMMAND[2]:
            ans.popleft()
        elif com[0] == COMMAND[3]:
            ans.pop()
    print(" ".join(ans))