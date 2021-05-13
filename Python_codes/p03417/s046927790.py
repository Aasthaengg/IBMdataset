n, m =map(int, input().split())

if n>=2 and m>=2:
	print(n*m-2*max(n,m)-2*(min(n,m)-2))
elif n==1 and m==1:
	print(1)
elif n==1 or m==1:
	print(max(n,m)-2)
