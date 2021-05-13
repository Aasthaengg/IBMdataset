N,K = map(int,input().split())

if K%2 == 0:
	count1 = N//K
	count2 = (N+N%K)//K
	ans = count1 ** 3 + count2 ** 3 

if K%2 == 1:
	count3 = N//K
	ans = count3 ** 3

print(ans)