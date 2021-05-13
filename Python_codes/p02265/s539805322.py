import collections
a=collections.deque()
for _ in range(int(input())):
    b=input()
    if b[0]=='i':a.appendleft(b[7:])
    elif b[6]==' ':
        try:a.remove(b[7:])
        except:pass
    elif len(b)>10:a.popleft()
    elif len(b)>6:a.pop()
print(*a)
