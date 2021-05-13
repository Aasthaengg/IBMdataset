n,mat = raw_input(),[ map(int,raw_input().split()) for i in range(2)]
mem = {}
def f(mat,i,j):
	if i<0 or j <0: return -float('inf')
	if i == 0 and j == 0: return mat[i][j] 
	if (i,j) not in mem:
		mem[(i,j)] =  mat[i][j] + max(f(mat,i-1,j),f(mat,i,j-1))
	return mem[(i,j)]
print f(mat,1,len(mat[0])-1)