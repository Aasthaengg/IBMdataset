import heapq
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
asum = sum(a)
c = []
csum = 0
num = []
for i,j in zip(a,b):
	if i<j:
		i = i + (j-i)
		ans += 1
	if i>j:
		heapq.heappush(num, -1*(i-j))
	csum += i


while csum>asum and len(num):
	i = heapq.heappop(num)*-1
	csum -= i
	ans += 1

if csum>asum: ans = -1
	
print(ans)

