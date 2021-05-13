from collections import deque
d = deque(range(1,10))
k = int(input())

for _ in range(k):
    ans = d.popleft()
    mod = ans % 10
    if mod != 0:
        d.append(ans * 10 + mod - 1)
    d.append(ans * 10 + mod)
    if mod != 9:
        d.append(ans * 10 + mod + 1)

print(ans)