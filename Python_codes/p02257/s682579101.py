def isPrime( x ):
	if 2 == x or 3 == x:
		return True
	if 0 == x&1:
		return False
	i = 3 
	while  i*i <= x:
		if 0 == x%i:
			return False
		i += 1
	return True


n = int( raw_input( ) )
nums = []
while 0 < n:
	nums.append( int( raw_input( ) ) )
	n -= 1
cnt = 0
for num in nums:
	if isPrime( num  ):
		cnt += 1

print( cnt )