import math
import collections
h,w = map(int,input().split())
c = [[0]*10]*10
for i in range(10):
	c[i] = list(map(int,input().split()))
a = [[0]*w]*h
for i in range(h):
	a[i] = list(map(int,input().split()))


def bellman_ford(s):
	d = [float('inf')]*10 # 各頂点への最小コスト
	d[s] = 0 # 自身への距離は0
	for i in range(10):
		update = False # 更新が行われたか
		for x, y, z in g:
			if d[y] > d[x] + z:
				d[y] = d[x] + z
				update = True
		if not update:
 			break
		# 負閉路が存在
		if i == 9:
			return -1
	return d

g = []
for i in range(10):
	for j in range(10):
		x,y,z = j,i,c[i][j]
		g.append([x,y,z])

MINCOST = bellman_ford(1)

sum = 0
for j in range(h):
	for i in range(0,10):
		sum += MINCOST[i]*collections.Counter(a[j])[i]
print(sum)