def Fibonacci(n, a1, a2):
	if n<1 : return a1
	return Fibonacci(n-1,a1+a2,a1)

print( Fibonacci( int(input()), 1, 0 ) )