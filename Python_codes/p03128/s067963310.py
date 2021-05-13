n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=1)
use_list = [2,5,5,4,5,6,3,7,6]

ans = [-1]*(n+1)
ans[0] = 0
for a in A:
	ma = use_list[a-1]
	for i in range(n+1):
		if ans[i] == -1:
			continue
		if i+ma > n:
			break
		ans[i+ma] = max(ans[i+ma],ans[i]*10+a)
print(ans[n])