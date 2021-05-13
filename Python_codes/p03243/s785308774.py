n = str(input())
memo = int( n[0] + n[0] + n[0] )
if int(n) <= memo:
	print(memo)
else:
	print(memo + 111)
