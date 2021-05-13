n = int(input())
a = [int(c) for c in input().split()]
a = sorted(a)
ret = n*(n-1)*(n-2)//6
for i in range(n):
	for j in range(i+1, n):
		low, high = 0, n-1
		pivot = -1
		while (low <= high):
			mid = low + (high - low)//2
			if (a[mid] >= a[i] + a[j]): 
				pivot = mid
				high = mid-1
			else: low = mid+1
		if (pivot != -1): ret -= n-pivot
print(ret) 
