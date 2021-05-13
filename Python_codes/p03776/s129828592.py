from sys import stdin

def combination_table(N):
	C = []
	for i in range(N+1):
		C.append([0] * (N+1))
	for i in range(N+1):
		for j in range(i+1):
			if (j==0 or j==i):
				C[i][j] = 1
			else:
				C[i][j] = C[i-1][j-1]+C[i-1][j]
	return C

if __name__ == "__main__":
	N, A, B = stdin.readline().split(" ")
	N = int(N)
	A = int(A)
	B = int(B)
	V = []
	line = stdin.readline().split(" ")
	unique_elements = dict()
	for e in line:
		V.append(int(e)) 
		if not int(e) in unique_elements:
			unique_elements[int(e)] = 1
		else:
			unique_elements[int(e)] += 1
	V.sort(reverse=True)

	C = combination_table(N)

	# find optimal selections between A and B
	a_th_val_pos = 0
	a_th_val_num = 0
	highest_avg = float(sum(V[:A])) / float(A)
	for i in range(N):
		if V[i] == V[A-1]:
			a_th_val_num += 1
			if i < A:
				a_th_val_pos += 1


	cnt = 0
	if a_th_val_pos == A:
		for i in range(A, B+1):
			cnt += C[a_th_val_num][i]
	else:
		cnt += C[a_th_val_num][a_th_val_pos]

	print ("{:6f}".format(highest_avg))
	print (cnt)
