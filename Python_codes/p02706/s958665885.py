a, b = input().split()
s = list(map(int, input().split())) 
day = int(a) - sum(s) 
if day>=0:
  print(day)
else:
  print('-1')