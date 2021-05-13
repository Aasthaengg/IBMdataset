n, k = [int(x) for x in input().split()]

if k is 1:
	max_diff = 0
else:
	max_diff = n - k
    
print(max_diff)
