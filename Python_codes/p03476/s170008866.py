def generate_is_prime_sieve(N):
	is_prime = [True]*(N+1)
	is_prime[0] = is_prime[1] = False
	for p in range(2,N+1):
		if is_prime[p]:
			for n in range(2*p,N+1,p):
				is_prime[n] = False
	dummy=[x for x in is_prime]
	for p in range(2,N+1):
		if is_prime[p] and is_prime[(p+1)//2]:
			dummy[p]=True
		else:
			dummy[p]=False
	return dummy
def partial_sums(N):
	something=generate_is_prime_sieve(N)
	counter=0
	partial_sum=[0]*(N+1)
	for i in range(N+1):
		if something[i]:
			counter+=1
		partial_sum[i]=counter
	return partial_sum	
N=partial_sums(10**5+1)
for i in range(int(input())):
	counter=0
	a,b=[int(x) for x in input().split()]
	print(N[b]-N[a-1])

