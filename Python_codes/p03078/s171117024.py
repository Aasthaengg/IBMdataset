import collections
import heapq

x,y,z,t = map(int, raw_input().split(' '))
mat = [map(int,raw_input().split(' ')) for _ in range(3)]
for ii in range(len(mat)): mat[ii].sort(key = lambda x:-x)

seen,heap = set([(0,0,0)]),[(-mat[0][0]-mat[1][0]-mat[2][0], 0,0,0)]


while(heap and t):
	u,i,j,k = heapq.heappop(heap)
	print -u
	t-=1
	for nei in [(i+1,j,k), (i,j+1,k), (i,j,k+1)]:
		if nei not in seen and all([0<=nei[ii]<len(mat[ii]) for ii in range(3)]):
			seen.add(nei)
			vv = -sum([mat[ii][vvv] for ii,vvv in enumerate(nei)])
			heapq.heappush(heap,(vv,nei[0],nei[1],nei[2]))
