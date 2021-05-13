n = int(input())
if n==1:
	print(0)
elif n==2:
	print(2)
else:

	ans = ((10**n)-(9**n)-(9**n)+(8**n)) % ((10**9)+7)
	print(ans)