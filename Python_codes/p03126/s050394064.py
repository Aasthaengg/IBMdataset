n,m = map(int,input().split())
kl,al = [],[]
for _ in range(n):
	k,*a = list(map(int,input().split()))
	kl.append(k)
	al.append(a)
ans = [0]*(m+1)
cnt = 0
for i in range(n):
	for j in range(kl[i]):
		inx = al[i][j]
		ans[inx] += 1
for t in range(m+1):
	if ans[t] == n:
		cnt += 1
print(cnt)