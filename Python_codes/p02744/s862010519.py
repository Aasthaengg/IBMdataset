from collections import deque

n = int(input())
if n == 1:
    print('a')
else:
    q = deque(['a'])
    while q:
        x = q.popleft()
        l = len(x)
        s = len(set(x))
        for i in range(s+1):
            nx = x + chr(i + 97)
            if l + 1 == n:
                print(nx)
            if l < n - 1:
                q.append(nx)
