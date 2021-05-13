a = int(input())
snk = 1
for i in range(1, a+1):
  snk *= i
  if snk > 1000000007:
    snk %= 1000000007
print(snk%1000000007)