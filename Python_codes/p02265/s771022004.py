from collections import deque
def insert(x,a):
    a.appendleft(x)
def delete(x,a):
    if x in a:
        a.remove(x)
    else:
        return
def deletefirst(a):
    a.popleft()
def deletelast(a):
    a.pop()
n=input()
a=deque()
for i in xrange(n):
    s=raw_input().split()
    if s[0]=="insert":
        insert(s[1],a)
    elif s[0]=="delete":
        delete(s[1],a)
    elif s[0]=="deleteFirst":
        deletefirst(a)
    else:
        deletelast(a)
print(" ".join(a))