import sys
input = sys.stdin.readline

# B - Similar Arrays
def count_simular_arrays(arr):
	ans = 0
	
	for a in arr:
		for n in a:
			if n % 2 == 0:
				ans += 1
				break

	return ans


import copy

n = int(input())
a = list(map(int, input().split()))
arr = []

for i in range(-1, 2):
	arr.append([a[0] + i])

for i in range(1, n):
	copied = copy.deepcopy(arr)
	arr.clear()
	
	for c in copied:
		for j in range(-1, 2):
			arr.append(c + [a[i]+j])

print(count_simular_arrays(arr))