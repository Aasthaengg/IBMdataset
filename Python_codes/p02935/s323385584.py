import collections

n = int(input())
v = list(map(int, input().split()))

v.sort()

v = collections.deque(v)

ans = v.popleft()

for i in range(n-1):
    a = v.popleft()
    ans = (ans + a)/2

print(ans)