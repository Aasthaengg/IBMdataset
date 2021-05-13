
n = int(input())

res = 0


for a in range(1,n):
	res += ((n-a - 1) // a) + 1
print(res)
