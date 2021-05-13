(n, m, l) = map(int, raw_input().split())

A = []
for i in xrange(0,n):
	line_A = map(int, raw_input().split())
	A.append(line_A)

B = []
for j in xrange(0,m):
	line_B = map(int, raw_input().split())
	B.append(line_B)

C = []
for x in xrange(0,n):
	temp_list = []
	for y in xrange(0,l):
		temp = 0
		for z in xrange(0,m):
			temp = temp + A[x][z] * B[z][y]

		temp_list.append(temp)
		
	C.append(temp_list)
	temp_list = []
			

for k in xrange(0,n):
	if k > 0:
		print
	for h in xrange(0,l):
		print C[k][h],
print