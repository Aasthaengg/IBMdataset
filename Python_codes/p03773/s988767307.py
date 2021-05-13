a, b = map(int, input().split())
r = a + b
if r >= 24:
	r = r - 24
print(r)