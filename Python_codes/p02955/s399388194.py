n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

def prime_factorize(num):
	x = 1
	fcts = []
	while x * x <= num:
	    if num % x == 0:
	        fcts.append(x)
	        fcts.append(num // x)
	    x += 1
	fcts.sort(reverse = True)
	return fcts

def num_operation(l):
	# lでAの要素を割り切るために必要な操作の回数
	nums_div1 = sorted([x % l for x in nums])
	nums_div2 = [(l - x) % l for x in nums_div1]
	min_op = 10 ** 10

	lf = 0
	rg = sum(nums_div2)
	if rg % l == 0:
		min_op = rg

	for i in range(n):
		lf += nums_div1[i]
		rg -= nums_div2[i]
		if (lf - rg) % l == 0:
			min_op = min(min_op, max(lf, rg))
	return min_op

sum_nums = sum(nums)
fcts = prime_factorize(sum_nums)

for fct in fcts:
	if num_operation(fct) <= k:
		print(fct)
		break
