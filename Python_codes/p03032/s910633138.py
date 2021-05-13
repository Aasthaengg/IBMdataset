n,k = map(int,input().split())
from collections import deque
au = list(map(int,input().split()))
left = [0 for i in range(n)]
right = [0 for i in range(n)]
left[0] = au[0]
right[0] = au[-1]
ans = 0
for i in range(n-1):
    left[i+1] = left[i] + au[i+1]
    right[i+1] = right[i] + au[n-i-2]
p = min(n,k)
for a in range(p+1):
    for b in range(p+1-a):
        d = deque(au)
        x = []
        y = 0
        for i in range(a):
            u = d.popleft()
            x.append(u)
            y += u
        for j in range(b):
            v = d.pop()
            x.append(v)
            y += v
        x.sort(reverse = True)
        for ue in range(k-a-b):
            if len(x) > 0 and x[-1] < 0:
                y -= x.pop()
            else:
                break
        ans = max(ans,y)
print(ans)