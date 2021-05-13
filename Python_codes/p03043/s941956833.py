import math
#N = int(input())
#S = str(input())
#A, B = map(int, input().split())
#C = list(map(int, input().split()))

N, K = map(int, input().split())

ans = 0
for i in range(1, N + 1):
  if i < K:
    tt = math.log2(K/i)
    if tt % 1 == 0:
      time = int(tt)
    else:
      time = int(tt) + 1
    ans += (1 / N) * ((1 / 2) ** time)
  else:
    ans += (1/ N)
#  print(time, ans)
  
print(ans)  