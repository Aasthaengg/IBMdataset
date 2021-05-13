n = int(input())
f = [int(input()) for _ in range(n)]
f = [0] + f
vis = [0] * (n + 1)
s , flag , ans = 1 , 0 , 0
vis[s] = 1
while f[s] != 2:
	if vis[f[s]] == 1:
		flag = 1
		break
	s = f[s]
	vis[s] = 1
	ans+=1

if (flag):
	print(-1)
else:
	print(ans+1) 