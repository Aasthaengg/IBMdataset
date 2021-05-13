from collections import deque
n=int(input())
a=list(map(int,input().split()))
b=deque()
if n%2==0:
    for i in range(n):
        if i%2==0:
            b.append(str(a[i]))
        else:
            b.appendleft(str(a[i]))
    print(" ".join(b))
else:
    for i in range(n):
        if i%2==0:
            b.appendleft(str(a[i]))
        else:
            b.append(str(a[i]))
    print(" ".join(b))
