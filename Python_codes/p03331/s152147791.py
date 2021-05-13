Max = 1000000
def digit_sum(n):
	res = 0
	while n>0:
		res += int(n%10)
		n /= 10
	return res

N = int(input())
if N==10 or N==100 or N==1000 or N==10000 or N==100000:
	print(10)
else:
	print(digit_sum(N))