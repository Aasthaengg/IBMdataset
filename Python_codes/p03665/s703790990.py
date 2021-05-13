import math

N,P = map(int,input().split())
A = list(map(int,input().split()))

remainders = [a%2 for a in A]

odd = remainders.count(1)
even = remainders.count(0)

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

ans = 0
for n in range(N+1):
  for p in range(P,n+1,2):
    if odd >= p and even >= n-p:
      ans += combinations_count(odd,p) * combinations_count(even,n-p)

print(ans)