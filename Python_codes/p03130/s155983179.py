from sys import stdin
from itertools import groupby

li = [list(map(int,stdin.readline().rstrip().split())) for _ in range(3)]
lis = []
for i in range(3):
    for j in range(2):
        lis.append(li[i][j])
lis.sort()
lin = []
for key, value in groupby(lis):
    lin.append(len(list(value)))
lin.sort()
if lin == [1,1,2,2]:
    print("YES")
else:
    print("NO")