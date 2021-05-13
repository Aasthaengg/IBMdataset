import collections
import heapq

x,y,z,t = map(int, raw_input().split(' '))
xs = map(int,raw_input().split(' '))
xs.sort(key = lambda x:-x)
ys = map(int,raw_input().split(' '))
ys.sort(key = lambda x:-x)
zs = map(int,raw_input().split(' '))
zs.sort(key = lambda x:-x)
mat = [xs,ys,zs]
heap = [(-mat[0][0]-mat[1][0]-mat[2][0], 0,0,0)]
seen = set([(0,0,0)])
res = []
while(heap and t):
	u,i,j,k = heapq.heappop(heap)
	print -u
	res.append(-u)
	t-=1
	for nei in [(i+1,j,k), (i,j+1,k), (i,j,k+1)]:
		if nei not in seen and all([0<=nei[ii]<len(mat[ii]) for ii in range(3)]):
			seen.add(nei)
			vv = mat[0][nei[0]] + mat[1][nei[1]] + mat[2][nei[2]]
			vv *= -1
			heapq.heappush(heap,(vv,nei[0],nei[1],nei[2]))
