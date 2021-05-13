n = int(input())
a = list(map(int,input().split()))
pos = set()

# n桁分のbit探索
for i in range(1 << n):
    point = 0
    for j in range(n):
        # j個目の商品が含まれるか
        if (i >> j)&1:
            point += a[j]
    pos.add(point)

q = int(input())
m = list(map(int,input().split()))

for i in m:
    if i in pos:
        print("yes")
    else:
        print("no")
