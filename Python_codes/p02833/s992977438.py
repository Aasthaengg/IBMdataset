from decimal import getcontext, Decimal
getcontext().prec = 1

N = int(input())
if N % 2 == 1:
	print(0)
else:
	ans = 0
	if N <= 9:
		pass
	else:
		ans += N//10
		N //= 10
		while N >= 5:
			ans += N//5
			N //= 5
	print(ans)