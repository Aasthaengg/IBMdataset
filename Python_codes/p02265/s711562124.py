from collections import deque
n = int(raw_input())
R = deque()
for i in xrange(n):
    L = raw_input().split()
    order = L[0]
    value = 0
    if len(L) > 1:
        value = int(L[1])
    if order == 'insert':
        R.appendleft(value)
    if order == 'delete' and value in R:
        R.remove(value)
    if order == 'deleteFirst':
        R.popleft()
    if order == 'deleteLast':
        R.pop()
print ' '.join(map(str, R))