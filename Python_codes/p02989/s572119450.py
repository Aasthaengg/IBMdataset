def dividek(arr, n):
	arr.sort()
	return arr[n//2] - arr[(n//2)-1]
n = int(input())
arr = list(map(int, input().split()))
print(dividek(arr, n))