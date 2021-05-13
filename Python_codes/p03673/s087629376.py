from collections import deque

n = int(input())
a = list(map(int, input().split()))

order = n%2
ans = deque([])
for i in range(n):
    if i%2 == order:
        ans.append(a[i])
    else:
        ans.appendleft(a[i])
for el in ans:
    print(el, end=' ')