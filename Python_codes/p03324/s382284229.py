n=list(map(int, input().split()))

if n[1]==100:
  print((n[1]+1)*(100**n[0]))
else:
  print(n[1]*(100**n[0]))