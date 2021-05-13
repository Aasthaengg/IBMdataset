def check(p, n, w, k):
	temp = 0
	for i in range(n):
		if w[i] > p:
			return False
		if temp + w[i] > p:
			temp = 0
			k -= 1
			if k < 0:
				return False
		temp += w[i]
	if k == 0:
		return False
	else:
		return True

def main():
	n, k = map(int,input().split())
	w = []
	for _ in range(n):
		w += [int(input())]
	pmin = 0
	pmax = 10**10
	while True:
		if pmin >= pmax:
			print(pmin)
			break
		if check(int((pmin+pmax)/2),n,w,k):
			pmax = int((pmin+pmax)/2)
		else:
			pmin = int((pmin+pmax)/2)+1

main()
