from collections import deque
n,k = map(int,input().split())
sl = list(input())

d = deque([])
ans = 0
before = "1"
tmp = 0
p = 0
for s in sl:
    if before == s:
        p += 1
    else:
        d.append(p)
        tmp += p
        p = 1
        before = s
    if len(d) == 2 * k + 1:
        ans = max(tmp, ans)
        tmp -= d.popleft()
        tmp -= d.popleft()
else:
    d.append(p)
    tmp += p
    ans = max(tmp, ans)

print(ans)