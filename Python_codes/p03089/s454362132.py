from collections import deque
import numpy as np

N = int(input())
B = list(map(int, input().split()))
Ans = deque()
Sa = np.zeros(N)
for a, b in enumerate(B):
    Sa[a] = a-b+1
while 0 in Sa:
    for i in range(N)[::-1]:
        if Sa[i] == 0:
            Ans.appendleft(B[i])
            Sa[i:] -= 1
            break
if len(Ans) != N:
    print(-1)
else:
    for i in range(len(Ans)):
        a = Ans.popleft()
        print(a)
