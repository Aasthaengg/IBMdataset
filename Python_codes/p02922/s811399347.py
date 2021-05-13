A, B = map(int, input().split())
 
if (B-1)%(A-1) == 0:
  print(int((B-1)/(A-1)))
else:
  print(int((B-1)//(A-1) +1))