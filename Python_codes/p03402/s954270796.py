A, B = map(int, input().split())

white = [["#"] * 100 for i in range(50)]
black = [["."] * 100 for i in range(50)]
A, B = A-1, B-1

row = 0
line = 0

for i in range(A):
	white[line][row] = "."
	row += 2
	if row >=100:
		row = 0
		line += 2

row = 0
line = 1
for i in range(B):
	black[line][row] = "#"
	row += 2
	if row >= 100:
		row = 0
		line += 2

ans = white + black
print(100, 100)
for a in ans:
	print("".join(a))
