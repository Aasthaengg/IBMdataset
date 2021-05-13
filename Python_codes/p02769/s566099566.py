[N,K] = list(map(int,input().split()))

mod = pow(10,9)+7

kaijo = [1]
for i in range(1,N+1): 
  kaijo.append(kaijo[i-1]*i % mod)

s =0
for m in range((K+1)*(N>K)+(N)*(K>=N)):
  s += (kaijo[N]*pow((kaijo[m]*kaijo[N-m]),mod-2,mod ))%mod * (kaijo[N-1]*pow((kaijo[m]*kaijo[N-1-m]),mod-2,mod ) )%mod
  s = s%mod

print(s)