n,m,d = (int(i) for i in input().split()) 
ans = 0.

if d == 0:
	ans = ( m - 1 ) / n
else:
	ans = 2 * ( n - d ) * ( m - 1 )
	ans = ans / (n * n )


print(ans)