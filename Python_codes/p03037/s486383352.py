n,m = map(int,input().split(" "))

lr = []

ming = 0
maxg = 10 **6

for i in range(m):
    a,b = map(int,input().split(" "))
    lr.append((a,b))

for i in lr:
    if i[0] > ming:
        ming = i[0]
    if i[1] < maxg:
        maxg = i[1]

print(max([0, maxg - ming + 1]))