n = int(input())

alst = list(map(int, input().split()))
if 0 in alst:
  print(0)
  exit()
  
else:
  ans = 1
  for i in range(n):
    ans *= alst[i]
    if ans > 10**18:
      print('-1')
      exit()

  print(ans)