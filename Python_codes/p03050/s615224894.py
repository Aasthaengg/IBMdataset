def sol(N):
  ans = 0
  for i in range(1,int(N**.5)+1):
    if N%i == 0:
      if i != N//i and N%(N//i-1) != 0:
        ans += N//i-1
  return ans

N = int(input())
if N == 1:
  print(0)
else:
  print(sol(N))
