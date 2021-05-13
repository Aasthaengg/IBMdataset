from collections import deque
sa=list(input())
sb=list(input())
sc=list(input())
a=deque(sa)
b=deque(sb)
c=deque(sc)
k=a.popleft()
while True:
    if k=="a":
        if not a:
            print("A")
            exit()
        else:
            k=a.popleft()
    if k=="b":
        if not b:
            print("B")
            exit()
        else:
            k=b.popleft()
    if k=="c":
        if not c:
            print("C")
            exit()
        else:
            k=c.popleft()