N, P=map(int,input().split())
S = list(map(int,list(input())))

def ma25():
  ret = 0
  for i in range(N):
    if S[i]%P == 0:
      ret+=(i+1)
  print(ret)

def ma():
  dp = [0]*P
  dp[0] = 1
  r = 0
  for i in range(N-1,-1,-1):
    r = ((S[i]*pow(10,N-1-i,P))+r)%P
    dp[r] += 1
  ret = 0
  for m in dp:
    ret += m*(m-1)//2
  print(ret)

if P == 2 or P == 5:
  ma25()
else:
  ma()
