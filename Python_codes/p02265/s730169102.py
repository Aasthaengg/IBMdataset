# -*- coding: utf-8 -*-
n = input()
l = []
tail = 0
for i in xrange(n):
    cmd = raw_input().split()
    if cmd[0] == "insert":
        l.append(cmd[1])
    elif cmd[0] == "delete":
        try:
            l.pop(len(l) - l[::-1].index(cmd[1]) -1)
        except ValueError:
            pass
    elif cmd[0] == "deleteFirst":
        l.pop()
    elif cmd[0] == "deleteLast":
        tail += 1

print " ".join(l[tail:][::-1])