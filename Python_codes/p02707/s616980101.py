n = int(input())
arr = [int(x) for x in input().split()]
count = [0 for x in range(n)]
for i in arr:
	count[i-1]+=1
for i in count:
	print(i)
