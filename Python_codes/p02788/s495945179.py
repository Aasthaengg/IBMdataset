import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")



n,d,a = map(int, input().split())
xh = [None]*n
# h = [None]*n
for i in range(n):
    xh[i] = tuple(map(int, input().split()))
xh.sort()

r = 0
val = 0
from queue import deque
q = deque([])
s = 0
for l,(x,h) in enumerate(xh):
    bound = x+2*d
    while q and l>=q[0][1]:
        s -= q[0][0]
        q.popleft()
    while r<n and xh[r][0]<=bound:
        r += 1
    nokori = h - s
    if nokori>0:
        num = nokori//a + int(nokori%a!=0)
        val += num
        q.append((num*a, r))
        s += num*a
        
print(val)