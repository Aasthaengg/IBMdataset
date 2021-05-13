import sys
input = sys.stdin.readline

# B - Exactly N points
n = int(input())
m = 1
sum = 1

while sum < n:
	sum = (m + 1) * m / 2 
	m += 1

if m == 1:
	ans = [1]
else:
	ans = list(range(1, m))

try:
	ans.remove(sum - n)
except Exception:
	pass

for a in ans:
	print(a)