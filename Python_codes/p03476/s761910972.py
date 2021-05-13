def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    
    like=[False]*(n+1)
    for i in range(1,n+1,2):
        if(is_prime[i]==False):
            continue
        else:
            if(is_prime[int((i+1)/2)]==True):
                like[i]=True
            
    return  like
    #return [i for i in range(n + 1) if is_prime[i]]
q=int(input())
table=primes(10**5+10)
accum=[0]
for i in range(1,10**5+5):
        if(table[i]==True):
            accum.append(accum[i-1]+1)
        else:
            accum.append(accum[i-1])
for i in range(q):
    l,r=map(int,input().split())
    print(accum[r]-accum[l-1])