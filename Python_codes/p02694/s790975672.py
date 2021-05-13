import math

x = int(input())
an = 100
for i in range(1,10000):
  an  = 101*an//100
  if(an>=x):
    print(i)
    break