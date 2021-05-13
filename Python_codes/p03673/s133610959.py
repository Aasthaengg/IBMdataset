from collections import deque
d = deque()
N = int(input())
array = list(map(int,input().split()))
for i in range(N):
    if i%2==0:
        d.appendleft(array[i])
    else:
        d.append(array[i])
if N%2==0:
    d = reversed(d)
ans = ' '.join(map(str,d))
print(ans)