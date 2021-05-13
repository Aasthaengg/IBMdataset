a,b = list(map(int,input().strip().split()))

s = a+b
if s >= 10:
  print("error")
else:
  print(s)