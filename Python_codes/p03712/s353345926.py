h, w = map(int, input().split())
mat = [["#" for i in range(w+2)] for j in range(h+2)]
pix = []
for i in range(h):
	s = input()
	pix.append(s)
for i in range(1, h+1):
	for j in range(1, w+1):
		mat[i][j] = pix[i-1][j-1]
for i in mat:
	print("".join(i))