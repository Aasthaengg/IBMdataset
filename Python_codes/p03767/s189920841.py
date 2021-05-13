import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
from queue import deque
q = deque(a)
ans = 0
for i in range(n):
    v1,v2,v3 = q.popleft(), q.popleft(), q.pop()
    ans += v2
print(ans)