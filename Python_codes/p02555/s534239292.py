S = int(input())
mod = 10**9+7
memo = [-1]*(S+1)
memo[0] = 1
def redis(s):
  if memo[s] != -1:
    return memo[s]
  else:
    if s < 3:
      memo[s] = 0
      return 0
    elif s < 6:
      memo[s] = 1
      return 1
    else:
      tmp = 0
      for num in range(s-2):
        tmp += redis(num)%mod
      memo[s] = tmp
      return tmp%mod
print(redis(S))
    


