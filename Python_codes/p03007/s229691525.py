from collections import deque
n = int(input())
a = list(map(int, input().split()))
a.sort()
a = deque(a)

left = a.popleft()
right = a.pop()

ans = []
for i in a:
    if i > 0:
        ans.append((left, i))
        left -= i
    else:
        ans.append((right, i))
        right -= i
else:
    ans.append((right, left))

print(right-left)
for x, y in ans:
    print(x, y)
