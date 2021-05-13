import sys
from collections import deque

n,m = map(int, sys.stdin.readline().rstrip("\n").split())
bridges = [[] for _ in range(n)]
done = [False]*n
for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip("\n").split())
    bridges[a-1].append(b-1)
    bridges[b-1].append(a-1)
d = deque()
ans = -1
for i in range(n):
    if not done[i]:
        done[i] = True
        d.append(i)
        while d:
            cp = d.pop()
            for np in bridges[cp]:
                if not done[np]:
                    done[np] = True
                    d.append(np)
        ans += 1
print(ans)