import sys

def print_arr(arr):
	for i in range(len(arr)):
		sys.stdout.write(str(arr[i]))
		if i != len(arr) - 1:
			sys.stdout.write(' ')
	print()

n = int(input())
arr = list(map(int, input().split()))

swap_count = 0
for i in range(n):
	mini = i
	for j in range(i, n):
		if arr[j] < arr[mini]:
			mini = j
	if mini != i:
		arr[i] = arr[i] ^ arr[mini]
		arr[mini] = arr[i] ^ arr[mini]
		arr[i] = arr[i] ^ arr[mini]
		swap_count += 1

print_arr(arr)
print(swap_count)

