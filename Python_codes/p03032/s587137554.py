from heapq import heapify,heappush,heappop
import math

n,K = map(int,input().split())
v = list(map(int,input().split()))

ans = 0
sum_d = 0
d = []
heapify(d)
# i = 操作回数
# j = 取る回数 (i-j = 捨てる回数)
# k = 左から取る回数 (j-k = 右から取る回数)
for i in range(1,K+1):
	for j in range(math.ceil(i/2),min(i+1,n+1)):
		for k in range(j+1):
			#print(i,j,k,j-k,i-j,ans)
			# 左から取る
			for l in range(k):
				heappush(d,v[l])
				sum_d += v[l]
			# 右から取る
			for l in range(j-k):
				heappush(d,v[-l-1])
				sum_d += v[-l-1]
			for l in range(i-j):
				sum_d -= heappop(d)
			ans = max(sum_d,ans)
			sum_d = 0
			d = []
			heapify(d)
print(ans)
