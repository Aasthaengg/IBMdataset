N, L = map(int,input().split())
def f(i):
	return L+i-1
def eat(bad):
	return sum([f(i) for i in range(1,N+1) if i!=bad])
best = 10**18
best_val = -1
for i in range(1,N+1):
	x = abs(eat(i)-eat(-1))
	if x < best:
		best = x
		best_val = eat(i)
print(best_val)