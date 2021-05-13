import itertools
mylist = [0, 1]
n = int(input().rstrip())

mise = [list(map(int, input().rstrip().split())) for i in range(n)]
mine = [list(map(int, input().rstrip().split())) for i in range(n)]

maxnum = - float('inf')
for i in itertools.product(mylist, repeat = 10):
    if sum(i) == 0:
        continue
    sell = 0
    for j, k in zip(mise, mine):
        temp = 0
        for l in range(10):
            if j[l] == i[l] and j[l] == 1:
                temp += 1
        sell += k[temp]
    maxnum = max(maxnum, sell)
print(maxnum)