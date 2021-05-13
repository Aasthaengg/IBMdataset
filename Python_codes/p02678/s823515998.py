from collections import deque

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

tai = [False] * (n+1)
tai[1] == True
ans = [0] * (n+1)

tri = deque([1])
while len(tri) > 0:
    num = tri.popleft()
    for i in lst[num]:
        if tai[i]:
            continue
        tri.append(i)
        tai[i] = True
        ans[i] = num

print('Yes')
for i in range(2, n+1):
    print(ans[i])