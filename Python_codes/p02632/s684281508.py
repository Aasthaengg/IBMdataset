K = int(raw_input())
S = raw_input().strip()
L = len(S)

P = 10**9 + 7

facts = [0 for _ in xrange(L + K)]
finvs = [0 for _ in xrange(L + K)]
facts[0] = 1
for i in xrange(1, L+K):
  facts[i] = (i*facts[i-1]) % P

finvs[L+K-1] = pow(facts[L+K-1], P-2, P)
for i in xrange(L+K-2, -1, -1):
  finvs[i] = (finvs[i+1]*(i+1)) % P

ans = 0
for k in xrange(0, K+1):
  ncr = (facts[k+L-1]*finvs[k]*finvs[L-1]) % P
  ans += ncr * pow(25, k, P) * pow(26, K-k, P)
  ans %= P

print ans
