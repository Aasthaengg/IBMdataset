import math
mod = 10**9+7

n,m = map(int,input().split())

m_p = {}
m_t = m
for i in range(2,math.ceil(m**0.5)+1) :
  if m_t%i == 0:
    m_p[i] = 0
    for j in range(10**9) :
      m_p[i] += 1
      m_t //= i
      if m_t%i != 0 :
        break
if m_t != 1 :
  m_p[m_t] = 1
  
ans = 1
for v in m_p.values() :
  # nCr = c1/c2　とおく
  # n = v+(n-1)
  # r = v
  c1 = 1
  # c1 = (v+n-1)*(v-1+n-1)*...*((v-(v-1))+n-1)の計算
  for i in range(v) :
    c1 = c1*(v-i+n-1)%mod
  # 1/c2 = (1/v)*(1/(v-1))*...*(1/1)の計算
  c2 = 1
  for i in range(v) :
    c2 = c2*pow(v-i,mod-2,mod)%mod
  ans *= c1*c2%mod
  ans %= mod
  
print(ans)