S = input()
m = 's'
n = 'es'
if S[-1] == 's':
	res = "".join((S,n))
	print(res)
else:
	res1 = "".join((S,m))
	print(res1)