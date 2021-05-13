import bisect
import math

n, h = map(int, input().split())
A, B = [], []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
atk = max(A)
B.sort(reverse=True)
L = [0]
for i in range(n):
    if B[i] >= atk:
        L.append(L[-1] + B[i])
    else:
        break
if L[-1] >= h:
        ans = bisect.bisect_left(L, h)
else:
    h -= L[-1]
    ans = len(L) - 1 + math.ceil(h / atk)
print(ans)
