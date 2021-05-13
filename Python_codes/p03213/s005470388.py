def factorization(n):
    d = {}
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            d[i] = cnt
    if temp!=1:
        d[temp] = 1
    if len(d) == 0:
        d[n] = 1
    return d

N = int(input())
fac_dict = {}
for n in range(1, N+1):
  d = factorization(n)
  for p in d:
    if p in fac_dict:
      fac_dict[p] += d[p]
    else:
      fac_dict[p] = d[p]

# [74個以上, 24個以上, 14個以上, 4個以上, 2個以上]
num_prime = [0, 0, 0, 0, 0]
for p in fac_dict:
  num = fac_dict[p]
  if num >= 2:
    num_prime[4] += 1
    if num >= 4:
      num_prime[3] += 1
      if num >= 14:
        num_prime[2] += 1
        if num >= 24:
          num_prime[1] += 1
          if num >= 74:
            num_prime[0] += 1

ans = 0
ans += num_prime[0] # A = p**74 のパターン
ans += num_prime[1] * (num_prime[4]-1) # A = p1**2 * p2**24 のパターン
ans += num_prime[2] * (num_prime[3]-1) # A = p1**4 * p2**14 のパターン
ans += (num_prime[3]*(num_prime[3]-1)//2) * (num_prime[4]-2) # A = p1**2 * p2**4 * p3**4 のパターン
print(ans)