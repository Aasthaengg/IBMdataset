import collections,sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
N = I()
a = sorted(LI())
deque = collections.deque()
for x in a:
    deque.append(x)
ans = 0
for _ in range(N):
    deque.popleft()
    deque.pop()
    ans += deque.pop()
print(ans)
