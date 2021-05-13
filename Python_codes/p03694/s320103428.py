n = int(input())
arr = list(map(int, input().split()))
mn = 100000000
mx =0
for i in arr:
	mn = min(mn , i)
	mx = max(mx , i)

print(mx-mn)