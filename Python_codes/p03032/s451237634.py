# D
n, k = map(int, input().split())
v = list(map(int, input().split()))
q = []
ans = 0
for a in range(min(n, k) + 1):
    for b in range(min(n, k) - a + 1):
        # print(a, b)
        if a == 0:
            pass
        else:
            q.extend(v[:a])
        if b == 0:
            pass
        else:
            q.extend(v[-b:])
        q.sort()
        pick = k - (a + b)
        for i in range(min(pick, len(q))):
            # print(i, q)
            if q[0] < 0:
                q.reverse()
                q.pop()
                q.reverse()
            else:
                break
        s = sum(q)
        # print(q, pick, q[:pick], s)
        if ans < s:
            ans = s
        q.clear()
print(ans)
