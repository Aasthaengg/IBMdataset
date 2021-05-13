c1 = list(input())
c2 = str(input())

c3 = "".join(c1[::-1])
if c2 == c3:
	print("YES")
else:
	print("NO")