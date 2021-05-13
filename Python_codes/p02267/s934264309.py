def linear_search(arr, key):
	arr.append(key)
	i = 0 
	while arr[i] != key:
		i += 1
		if i == n:
			return -1 
	return i 

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
count = 0 
for i in range(q):
	if linear_search(S, T[i]) != -1:
		count += 1
print(str(count))

