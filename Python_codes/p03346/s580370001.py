n = int(input())
l = [0]*(n+1)
for i in range(n):
    l[int(input())] = i
l = l[1:]

import sys
if n == 1:
    print(0)
    sys.exit()

m = 0
count = 1
for i in range(n-1):
    if l[i+1]>l[i]:
        count += 1
    else:
        m = max(m,count)
        count = 1
    m = max(m,count)
print(n-m)