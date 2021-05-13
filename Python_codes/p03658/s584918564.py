n , m = map(int , input().split())
arr = list(map(int , input().split()))
arr.sort()
arr = arr[::-1]
res =0
for i in range(0 , m):
	res = res+arr[i]
print(res)