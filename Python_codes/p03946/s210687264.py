n, t = map(int, input().split())
a = list(map(int, input().split()))


#最小値が更新された時にそれまでの利益の最大値を候補としてリストに追加
a.append(0)
mini = 10e10
maxval = 0
maxvals = []
for x in a:
    if mini > x:
        mini = x
        maxvals.append(maxval)
        maxval = 0
    else:
        maxval = max(maxval, x - mini)

print(maxvals.count(max(maxvals)))
#3 2
#100 50 200