import statistics
import math

n = int(input())
 
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))

b = [[],[]]
for i in range(n):
    b[0].append(a[i][0])
    b[1].append(a[i][1])

x = statistics.median(b[0])
y = statistics.median(b[1])

if n % 2 != 0:
    ans = y - x + 1

else:
    ans = round((y - x) * 2) + 1

print(ans)