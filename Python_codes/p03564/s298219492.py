def f(current, n,k):
	if n == 0:
		return current
	return min(f(2*current, n- 1,k), f(+k + current, n- 1, k)) 
print f(1,int(raw_input()), int(raw_input()))
