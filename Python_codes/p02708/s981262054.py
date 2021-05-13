N, K = list(map(int,input().split()))
MOD = 10**9 + 7

#取る個数が違った場合、その和は絶対同じ数にならない。
#n個とるとしたら最低値(lowest)は下(0)からn-1まで、最大値(highest)は上(N-0)からN-(n-1)までの和
#最小値から最大値は連続的にすべての値をとる。
#ただし、n=K~Nであるのでここはfor文

ans = 0
for n in range(K,N+2):
  lowest = n*(n-1) // 2
  highest = n*N - n*(n-1) // 2
  
  ans += highest - lowest + 1
  ans %= MOD
  
print(ans)