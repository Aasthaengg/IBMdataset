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
dp=[0]*(10**5+1)
bp=[0]*(10**5+1)
for i in primes(10**5):
  dp[i]=1
for i in range(1,10**5+1):
  bp[i]+=bp[i-1]
  if i%2==0:
    continue
  if dp[(i+1)//2]==1 and dp[i]==1:
    bp[i]+=1
Q=int(input())
for _ in range(Q):
  l,r=map(int,input().split())
  print(bp[r]-bp[l-1])