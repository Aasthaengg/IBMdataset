from collections import deque
n=int(raw_input())
q = deque()
for i in xrange(n):
    o = raw_input()
    if o == 'deleteFirst':  q.popleft()
    elif o == 'deleteLast': q.pop()
    else:
        c,p = o.split(); p = int(p)
        if c == 'insert': q.appendleft(p)
        elif c == 'delete':
            try: q.remove(p)
            except: pass
print ' '.join(map(str,q))