import bisect

N = int(input())
Bs = list(map(int, input().split()))

As = []
while Bs:
  f = 0
  for i in range(len(Bs)-1,-1,-1):
    if Bs[i] == i + 1:
      f = 1
      As.append(Bs.pop(i))
      break
  if f == 0:
    print('-1')
    exit()
    
for a in As[::-1]:
  print(a)