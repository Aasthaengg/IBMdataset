def COMB(a,b):
	if b > (a-b):
		b = a-b
	ans = 1
	for i in range(0,b):
		ans *= (a-i)
	for i in range(0,b):
		ans //= (b-i)

	return int(ans)

if __name__ == '__main__':
	N, A, B = map(int, input().split())
	v_lst = [int(p) for p in input().split()]

	v_lst.sort(reverse = True)

	count = 0

	for i in range(0,B-A+1):
		lst = v_lst[0:A+i]
		mean = sum(lst)/len(lst)
		if i == 0:
			nxt_mean = mean
		if mean == nxt_mean:
			a = v_lst.count(min(lst))
			b = lst.count(min(lst))
			count += COMB(a,b)
		else:
			break
		nxt_mean = mean

	print("{:.6f}".format(nxt_mean))
	print(count)