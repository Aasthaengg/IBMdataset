n = int(input())
arr = []
for i in range(0 , n):
	arr.append(int(input()))
tot = 0
for i in range( 0 , n):
	tot = tot+arr[i]
if tot%10!=0:
	print(tot)
else:
	res =0
	for i in range(0 , n):
		if (tot-arr[i])%10!=0:
			res = max(res, tot-arr[i])
	print(res)