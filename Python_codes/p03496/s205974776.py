import sys
from collections import deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n = int(readline())
lst1 = list(map(int,readline().split()))
ans = []
if abs(max(lst1)) > abs(min(lst1)):
    a = lst1.index(max(lst1)) + 1
    for i in range(n):
        ans.append([a,i+1])
    for i in range(n-1):
        ans.append([i+1,i+2])
else:
    a = lst1.index(min(lst1)) + 1
    for i in range(n):
        ans.append([a,i+1])
    for i in range(n-1,0,-1):
        ans.append([i+1,i])
print(len(ans))
for i,j in ans:
    print(i,j)
