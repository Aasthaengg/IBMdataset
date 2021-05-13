def main():
	N, A, B = map(int, input().split())
	v = list(map(int, input().split()))
	v.sort(reverse=True)
	ave_ans = sum(v[:A])/A
	cmp_v = v[A-1]
	cmp_v_in = 0
	cmp_v_out = 0
	def get_total(values):
		ans = 0
		for v in values:
			if v == cmp_v:
				ans += 1
		return ans
	cmp_v_in = get_total(v[:A])
	cmp_v_out = get_total(v[A:])
	fact = [0]*51
	fact[0] = 1
	fact[1] = 1
	for i in range(2, 51):
		fact[i] = fact[i-1]*i

	def C(n, k):
		return fact[n]//(fact[k]*fact[n-k])

	print(ave_ans)

	choose_ans = C(cmp_v_in+cmp_v_out, cmp_v_in)
	if cmp_v_in == A:
		for i in range(1, min(B-A+1, cmp_v_out+1)):
			choose_ans += C(cmp_v_in+cmp_v_out, cmp_v_in+i)
	print(choose_ans)

if __name__ == '__main__':
    main()