l = [len(c) for c in input().split("T")]
x, y = map(int, input().split())
bx = 1 << l.pop(0) + 8000
by = 1 << 8000
for i, d in enumerate(l):
	if i % 2:
		bx = (bx << d) | (bx >> d)
	else:
		by = (by << d) | (by >> d)
print("Yes" if bx & (1 << x + 8000) and by & (1 << y + 8000) else "No")