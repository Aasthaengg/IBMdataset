n = list(map(str, input().split()))
a, b = int(n[0]),int(n[2])
if n[1]=='+':
  print(a+b)
else:
  print(a-b)