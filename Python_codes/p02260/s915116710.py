import sys

def print_arr(arr):
	for i in range(len(arr)):
		sys.stdout.write(str(arr[i]))
		if i != len(arr) - 1:
			sys.stdout.write(' ')
	print()

def selection_sort(arr):
	cnt = 0
	n = len(arr)
	for i in range(n):
		mini = i
		for j in range(i + 1, n):
			if arr[j] < arr[mini]:
				mini = j
		if mini != i:
			temp = arr[i]
			arr[i] = arr[mini]
			arr[mini] = temp
			cnt += 1
	return cnt

n = int(input())
arr = list(map(int, input().split()))

cnt = selection_sort(arr)
print_arr(arr)
print(cnt)
