def comb(p,q,A,fact = None,factinv = None): #pCq modA
  if (q < 0) or (p < q):
    return 0
  q = min(q, p - q)
  return fact[p] * factinv[q] * factinv[p-q] % A
def main():
  mod = 10 ** 9 + 7
  n, k = map(int, input().split())
  
  fact = [1] #n!をmodで割ったあまり、0! = 1
  factinv = [1,1] #(n!)^(-1)をmodで割ったあまり
  inv = [0,1] #n^-1をmodで割ったあまり
  
  for a in range(2, n + 1):
    inv.append((-inv[mod % a] * (mod // a)) % mod)
  for i in range(1, n + 1):
    fact.append((fact[-1] * i) % mod)
  for j in range(2, n + 1):
    factinv.append((factinv[-1] * inv[j]) % mod)
  ans = 0
  for i in range(min(n,k+1)): #i:空の部屋の数
    ans = (ans + comb(n,i,mod,fact,factinv)*comb(n-1,i,mod,fact,factinv)) % mod
  print(ans)
main()