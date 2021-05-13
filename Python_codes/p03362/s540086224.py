def primes(n):
	is_prime = [True] * (n+1)
	is_prime[0] = False
	is_prime[1] = False
	for i in range(2, int(n**0.5)+1):
		if not is_prime[i]:
			continue
		for j in range(i*2, n+1, i):
			is_prime[j] = False
	return [i for i in range(n+1) if is_prime[i]]

N=int(input())
ans=[]
prime_numbers=primes(55555)
while True:
    cnt=0
    for n in prime_numbers:
        if n%5==1:
            ans.append(n)
            cnt+=1
        if cnt==N:
            break
    break
print(*ans)