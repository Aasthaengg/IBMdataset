N = int(input())
A = list(map(int,input().split()))
from collections import deque
d = {}
X = deque()
for i in range(N):
    x = A[i]
    if x not in d:
        d[x] = 1
        X.appendleft(x)
    else:
        d[x] += 1
ans = 0
from collections import deque
Y=deque()
while X:
    x = X.popleft()
    a = d[x]
    if a%2 == 0:
        ans += a-2
        Y.appendleft(x)
    else:
        ans += a-1

n = len(Y)
ans += ((n+1)//2)*2
print(N-ans)