import collections
N=int(input())
A=collections.deque()
for i in range(N):
    c=input()
    if c[0]=='i':
        A.appendleft(int(c.split()[1]))
    elif c[6]==' ':
        if int(c.split()[1]) in A:
            A.remove(int(c.split()[1]))
    elif c[6]=='F':
        A.popleft()
    elif c[6]=='L':
        A.pop()
print(*A)
