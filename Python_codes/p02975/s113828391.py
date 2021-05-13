N = int(input())
As = list(map(int, input().split()))
 
if N%3 != 0 and max(As) > 0:
  print('No')
  exit()
  
else:
  n = N//3
  ma = max(As)
  l = len(str(bin(ma))) - 2
  for i in range(l):
    c = 0
    for a in As:
      if (a>>i)%2 == 0:
        c += 1
    if c != n and c != N:
      print('No')
      exit()

print('Yes')