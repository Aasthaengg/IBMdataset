import math

S = int(input())
if S <= 10**9:
  print("{} {} {} {} {} {}".format(0,0,10**9,1,10**9-S,1))
else:
  print("{} {} {} {} {} {}".format(0,0,10**9,1,(10**9)*math.ceil(S/(10**9))-S,math.ceil(S/(10**9))))