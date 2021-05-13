from math import sqrt
while True:
      n = int(input())
      if n == 0:
          break
      else:
          scores = list(map(int, input().split()))
          ave = float(sum(scores)) / n
          numerator = 0
          for s in scores:
              numerator += (s - ave)**2
          alpha = numerator / n
          print(sqrt(alpha))