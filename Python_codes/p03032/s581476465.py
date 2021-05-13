#template
def inputlist(): return [int(k) for k in input().split()]
#template
N,K = inputlist()
V = inputlist()
n = min(N,K)
ans = 0
from collections import deque
for a in range(n+1):
    for b in range(n+1):
        li = []
        if a+b > n:
            continue
        c = K-(a+b)
        que = deque(V)
        for i in range(a):
            k = que.popleft()
            li.append(k)
        for j in range(b):
            s = que.pop()
            li.append(s)
        li.sort()
        index = 0
        for i in range(len(li)):
            if li[i] < 0:
                index +=1
        na = min(index,c)
        suma = sum(li[na:])
        ans = max(ans,suma)

print(ans)