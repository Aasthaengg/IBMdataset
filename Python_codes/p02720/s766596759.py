from collections import deque
import sys
K = int(input())
q = deque([1,2,3,4,5,6,7,8,9])
num = 0
if K<=9:
    print(q[K-1])
    sys.exit()
for i in range(10**5):
    p = q.popleft()
    num += 1
    if num == K:
        print(p)
    if p%10 != 0:
        q.append(p*10+p%10-1)
    q.append(p*10+p%10)
    if p%10 != 9:
        q.append(p*10+p%10+1)