t = [int(v) for v in input().split(' ')]
n = t[0] + t[1]
n2 = t[2] + t[3]
 
if n > n2:
  print('Left')
elif n < n2:
  print('Right')
elif n == n2:
  print('Balanced')