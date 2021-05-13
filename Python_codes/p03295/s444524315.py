from operator import itemgetter
n,m = map(int,input().split())
a = [list(map(int,input().split())) for i in range(m)]
a = sorted(a, key=itemgetter(1))
bridge = [a[0][1]-1]
for i in range(1,m):
    if a[i][0] <= max(bridge):
        continue
    else:
        bridge.append(a[i][1]-1)
print(len(bridge))