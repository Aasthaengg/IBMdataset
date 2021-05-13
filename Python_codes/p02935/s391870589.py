def ing(arr):
	summ = arr[0]
	for i in range(1, len(arr)):
		summ = (summ + arr[i]) / 2
	return summ
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(ing(arr))