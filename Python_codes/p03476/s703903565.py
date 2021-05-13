def Sieve_of_Eratosthenes(n):
  is_prime = [True] * (n+1)
  is_prime[0] = False
  is_prime[1] = False
  for i in range(2, int(n**0.5)+1):
    if not is_prime[i]:
      continue
    for j in range(i*2, n+1, i):
      is_prime[j] = False
  return is_prime
  #return [i for i in range(n+1) if is_prime[i]]

def is_2017like(n):
  return is_prime[n] and is_prime[(n+1)//2]

is_prime = Sieve_of_Eratosthenes(10**5)
check = [is_2017like(n) for n in range(10**5 + 1)]
ans = [0]
for i in range(1, 10**5 + 1):
  if check[i]:
    ans.append(ans[-1] + 1)
  else:
    ans.append(ans[-1])

Q = int(input())
for _ in range(Q):
  l, r = map(int, input().split())
  print(ans[r] - ans[l-1])