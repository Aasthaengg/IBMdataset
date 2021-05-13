import collections
cc = collections.Counter([raw_input()[0] for _ in range(int(raw_input()))])


def dfs(i, total ,cumul, cc, k, s):
	if i == len(s) or k == 0:
		if k == 0: total[0] += cumul
		return 
	
	dfs(i+1, total, cumul * cc[s[i]], cc,k - 1, s)
	dfs(i+1, total, cumul, cc, k, s)

total = [0]
dfs(0, total, 1 , cc, 3, 'MARCH')
print total[0]