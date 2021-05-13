def make_divisors(n):
    divisors = set([])
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            if i != n // i:
                divisors.add(n//i)
    return divisors
N,M = map(int,input().split())
A=make_divisors(M)
ans=0
for i in A:
 if i<=M/N:
  ans=max(ans,i)
print(ans)