n = int(input())
s = [str(i) for i in input().split()]
a = set(s)
if len(a) == 3:
	print('Three')
else:
	print('Four')