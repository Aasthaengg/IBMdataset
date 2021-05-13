import sys
input = sys.stdin.readline
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return set([i for i in range(n + 1) if is_prime[i]])
sosuu = primes(55555)
N=int(input())
ans=[]
ct=0
for i in sosuu:
 if i%5==1:
  ans.append(i)
  ct+=1
 if ct==N:
  break
print(*ans)   
