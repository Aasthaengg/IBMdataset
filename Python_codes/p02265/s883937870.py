#ALDS1_3-C Elementary data structures - Doubly Linked List
import collections
import sys
q = collections.deque()
n=int(input())
_input = sys.stdin.readlines()
cmds={"insert":lambda cmd: q.appendleft(cmd[1]),
      "delete":lambda cmd: q.remove(cmd[1]) if (q.count(cmd[1]) > 0) else "none",
      "deleteFirst":lambda cmd: q.popleft(),
      "deleteLast": lambda cmd: q.pop()
     }

for i in range(n):
    cmd=_input[i].split()
    cmds[cmd[0]](cmd)
print(*q)