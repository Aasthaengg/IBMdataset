

n,k = map(int,input().split(" "))


arr = [i for i in range(1,n+1)]
# print(arr)
c = 0

for i in range(0,n-k+1):
	# print(arr[i:i+k])
	c += 1

print(c)