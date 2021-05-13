n = int(input())

minv = 1 << 30

def digit_sum(n):
	lst = list(map(int, str(n)))
	return sum(lst)

for i in range(1, n//2 + 1):
	a = i
	b = n - i
	minv = min(digit_sum(a) + digit_sum(b), minv)

print(minv) 
