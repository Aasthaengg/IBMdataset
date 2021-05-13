# 5で割って1余る素数だけで構成する
# すると任意の5つの組の和は5で割り切れるため、合成数となる
def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    return is_prime, table

ps = sieve(55555)[1]
N = int(input())
cands = []
for p in ps:
  if p%5 == 1:
    cands.append(p)
    if len(cands) == N:
      break

print(*cands)