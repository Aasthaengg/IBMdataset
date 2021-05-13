n, p = map(int, input().split())
A = list(map(int, input().split()))
o = 0
for a in A:
	if a % 2:
		o += 1
e = n - o
if o == 0 and p == 1:
	print(0)
else:
	print(2**e * 2**max(0, o - 1))