def primes(n):
    candidate = list(range(2, n+1))
    prime = []
    limit = n**0.5 + 1
    while True:
        p = candidate[0] 
        if limit <= p:
            prime.extend(candidate)
            break
        prime.append(p)

        candidate = [i for i in candidate if i % p != 0]
    return prime
N=int(input())
M=55555
L=primes(M)
L=[i for i in L if i%5==1]
S=L[:N]
S=list(map(str,S))
print(" ".join(S))