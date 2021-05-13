N,M,K = map(int,input().split())
flg = 0
for i in range(N+1) :
	for j in range(M+1) :
		if i * M + j * N - i * j * 2 == K : flg = 1
if flg : print("Yes")
else : print("No")