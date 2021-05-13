N = int(input())
As = [int(input()) for i in range(N)]
Bs = sorted(As, reverse = True)
ma = Bs[0]
ma2 = Bs[1]

for a in As:
  print(ma if a != ma else ma2)