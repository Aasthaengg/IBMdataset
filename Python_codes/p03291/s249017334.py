S = input()
lct_A = 0
lct_q = 0
rct_C = S.count("C")
rct_q = S.count("?")

MOD = 10**9 + 7

ans = 0
for s in S:
  if s == "C":
    rct_C -= 1
  elif s == "?":
    rct_q -= 1
  #print(s, lct_A, lct_q, rct_C, rct_q)
    
  if s == "B" or s == "?":
    ans += (lct_A * rct_C * pow(3, lct_q+rct_q, MOD)) % MOD
    if lct_q > 0:
      ans += (lct_q * rct_C * pow(3, lct_q+rct_q-1, MOD) ) % MOD
    if rct_q > 0:
      ans += (rct_q * lct_A * pow(3, lct_q+rct_q-1, MOD) ) % MOD
    if lct_q > 0 and rct_q > 0:
      ans += (lct_q * rct_q * pow(3, lct_q+rct_q-2, MOD) ) % MOD   
    ans %= MOD
    #print(" ", ans)
    
  if s == "A":
    lct_A += 1
  elif s == "?":
    lct_q += 1
    
print(ans % MOD)