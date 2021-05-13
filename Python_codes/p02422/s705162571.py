s = list(input())
q = int(input())
for i in range(q):
    cmd, a, b, *p = [x for x in input().split()]
    a = int(a)
    b = int(b)
    if cmd=='print':
        print(''.join(s[a:b+1]))
    if cmd=='reverse':
        stack = []
        for _ in range(b+1-a):
            stack.append(s.pop(a))
        for i in range(a, b+1):
            s.insert(i, stack.pop())
    if cmd=='replace':
        for i,c in zip(range(a,b+1), list(p[0])):
            s[i] = c

