def GSB(n):
	ans = -1
	for i in range(30):
		if n&(1<<i):
			ans = i
	return ans
def ans(a,b,c,d,M):
	other = [x for x in range(1<<M) if x not in [a,b,c,d]]
	print(*([a,b]+other+[c,d]+other[::-1]+[b,a,d,c]))

def solve(M,K):
	if K==0:
		arr = list(range(1<<M))
		print(*(arr+arr[::-1]))
	elif K==1:
		if M < 2:
			print(-1)
		else:
			ans(0,1,2,3,M)
	else:
		if M > GSB(K):
			a = 1<<GSB(K)
			b = K^a
			c = a+1
			d = K^c
			ans(a,b,c,d,M)
		else:
			print(-1)


solve(*map(int,input().split()))