from collections import defaultdict
n = int(input())
li = []
for i in range(n):
    x, y = map(int, input().split())
    li.append((x, y))
dd = defaultdict(lambda:0)
for i in range(n):
    for j in range(n):
        if i != j:
            dd[(li[i][0]-li[j][0], li[i][1]-li[j][1])] += 1
m = 0
for k in dd:
    m = max(dd[k],m)
print(n-m)