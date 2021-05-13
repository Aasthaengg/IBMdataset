from collections import Counter

def resolve():
	n = int(input())
	s = input()
	sum_e = [0]*(n+1)
	sum_w = [0]*(n+1)
	for i in range(n):
		ev = 1 if s[i] == 'E' else 0
		wv = 1 if s[i] == 'W' else 0
		sum_e[i+1] = sum_e[i] + ev
		sum_w[i+1] = sum_w[i] + wv
	ans = float('inf')
	if n == 2:
		print(1 if len(Counter(list(s)).keys()) == 2 else 0)
		return
	e_w = sum_e[-1] - sum_e[1]
	e_e = sum_w[n-1]
	ans = min(e_w, e_e)
	for i in range(n):
		v = sum_w[i-1] + (sum_e[-1] - sum_e[i])
		ans = min(ans, v)
	print(ans)
resolve()