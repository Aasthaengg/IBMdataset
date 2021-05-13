a,b,c,d = map(int,input().split())
sum_l = a + b
sum_r = c + d
if sum_l < sum_r:
  print('Right')
elif sum_l > sum_r:
  print('Left')
else:
  print("Balanced")