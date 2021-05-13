
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
L=primes(100000)
R=set([i for i in L if (i+1)//2 in L])
Q=int(input())
for i in range(Q):
  a,b=map(int,input().split())
  print(len([i for i in R if i>=a and i<=b]))