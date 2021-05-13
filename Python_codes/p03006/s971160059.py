from collections import defaultdict
n = int(input())
li = []
for i in range(n):
    xi,yi = map(int,input().split())
    li.append((xi,yi))
if n == 1:
    print(1)
    exit()
dic = defaultdict(int)
for i in range(n):
    for j in range(n):
        if i != j:
            xi = li[i][0]
            yi = li[i][1]
            xj = li[j][0]
            yj = li[j][1]
            dic[(xi-xj,yi-yj)] += 1
print(n-max(dic.values()))