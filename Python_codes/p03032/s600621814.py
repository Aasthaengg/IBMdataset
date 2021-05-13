from collections import deque
n, k = map(int, input().split())
v = list(map(int, input().split()))
ans = 0
for i in range(1, min(n, k+1)):
    vv = deque(v)
    q = deque(v[:i])
    for _ in range(i+1):
        tmp = list(q)
        tmp.sort()
        rem = k-i
        s = sum(tmp)
        for j in tmp:
            if rem==0 or j>=0:
                break
            s -= j
            rem -= 1
        ans = max(ans, s)
        q.pop()
        q.appendleft(vv.pop())
if k>=n:
    v.sort()
    rem = k-n
    s = sum(v)
    for j in v:
        if rem==0 or j>=0:
            break
        s -= j
        rem -= 1
    ans = max(ans, s)
print(ans)