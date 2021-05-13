import numpy as np
n = input()
a = map(int, raw_input().split())
max_i = np.argmax(a)
min_i = np.argmin(a)
ans = []
if abs(a[max_i]) >= abs(a[min_i]):
    for i in range(n):
        ans.append((max_i, i))
    for i in range(n-1):
        ans.append((i, i+1))
else:
    for i in range(n):
        ans.append((min_i, i))
    for i in range(n-1, 0, -1):
        ans.append((i, i-1))
print len(ans)
for x, y in ans:
    print (x+1), (y+1)