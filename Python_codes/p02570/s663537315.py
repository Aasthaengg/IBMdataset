D,T,S = map(int, input().split())
# Dm離れている, T分後, 分速Sm
if S * T >= D:
  print('Yes')
else:
  print('No')