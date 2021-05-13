from collections import deque
num=int(input())
a=deque()
for i in range(num):
    tmp=input().split()
    if tmp[0]=="insert":
        a.appendleft(tmp[1])
    if tmp[0]=="delete":
        if tmp[1] in a:
            a.remove(tmp[1])
    if tmp[0]=="deleteFirst":
        a.popleft()
    if tmp[0]=="deleteLast":
        a.pop()
print(" ".join(a))
