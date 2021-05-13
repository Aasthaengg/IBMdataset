data = input().split()

for n in range(len(data)):
	data[n] = int(data[n])

W, H, x, y, r = data

if (r <= x <= W - r) and (r <= y <= H - r):
	print("Yes")
else:
	print("No")