a,b = map(int,input().split())

if a*b%2 == 1:
	ans = 'Odd'
else:
	ans = 'Even'

print(ans)