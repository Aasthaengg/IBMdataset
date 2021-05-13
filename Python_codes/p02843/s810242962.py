stock = [1]+[0] * 100005
item = [100, 101, 102, 103, 104, 105]
for x in range(100001):
    for y in item:
        if stock[x - y]:
            stock[x] = 1

n = int(input())
if stock[n]:
    print(1)
else:
    print(0)