a, b, c = map(int, input().split())
b_a = b - a
c_b = c - b

if b_a == c_b:
	print("YES")
else:
	print("NO")