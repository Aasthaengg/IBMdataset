import collections
n = int(input())
*a, = map(int, input().split())
a.sort()
a = collections.deque(a)
ans = 0
while n:
    a.popleft()
    a.pop()
    ans += a.pop()
    n -= 1
print(ans)