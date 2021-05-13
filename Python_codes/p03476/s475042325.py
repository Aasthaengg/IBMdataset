Q = int(input())

N=10**5
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

F = primes(N)
F_2007=[]

a = [0]*(N+1)

for f in F:
    a[f] = 1

for f in F:
    if a[(f+1)//2] == 1:
        F_2007.append(f)
        
a = [0]*(N+1)
for f in F_2007:
    a[f] = 1
    
a_sum = [0]
for a_ in a:
    a_sum.append(a_sum[-1]+a_)
a_sum=a_sum[1:]

for q in range(Q):
    l,r = list(map(int,input().split()))
    print(a_sum[r] - a_sum[l-1])