def solve(i, j):
    if i == 0:
    	return True
    if j < n and A[0] <= i <= sum(A[j:]):
        x = solve(i-A[j], j+1)
        if x:
        	return x
        y = solve(i, j+1)
        if y:
        	return y

n = input()
A = sorted(map(int, raw_input().split()))
p = input()
m = map(int, raw_input().split())

for k in m:
	if solve(k, 0):
		print "yes"
	else:
		print "no"