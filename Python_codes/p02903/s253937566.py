import sys

H,W,A,B = map(int, input().split())

if A > -(-W//2) or B > -(-H//2):
	print("No")
	sys.exit()

orig_x = []
orig_y = []
for i in range(W):
	if i < A:
		orig_x.append(1)
		orig_y.append(0)
	else:
		orig_x.append(0)
		orig_y.append(1)

ans = []
for i in range(H):
	if i < B:
		ans.append(orig_x)
	else:
		ans.append(orig_y)

for i in range(H):
	for j in range(W):
		if j == W-1:
			print(ans[i][j])
		else:
			print(ans[i][j], end="")