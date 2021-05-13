n,k,s = map(int, input().split())

for i in range(n):
  if 0 < k:
    print(s)
    k -= 1
  else:
    if s - 1 < 100:
      print(s+1)
    else:
      print(s-1)