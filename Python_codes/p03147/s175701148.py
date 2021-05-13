N = int(input())
h_ls=list(map(int, input().split()))

kaisu=0

while max(h_ls)>0:
	M=h_ls.index(max(h_ls))
	takasa=h_ls[M]
	i=0
	while M+i<N and h_ls[min(M+i,N-1)]==takasa:
		h_ls[M+i]+=(-1)
		i+=1
	
	kaisu+=1

print(kaisu)
