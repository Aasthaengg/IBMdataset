n = input().split()
W = int(n[0])
H = int(n[1])
x = int(n[2])
y = int(n[3])
r = int(n[4])

top = y + r
bottom = y - r
right = x + r
left = x - r

if top <= H and bottom >= 0 and right <= W and left >= 0:
	print("Yes")
else:
	print("No")