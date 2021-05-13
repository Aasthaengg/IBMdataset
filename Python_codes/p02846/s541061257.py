import math

T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

sa = A1 * T1
sb = B1 * T1
ea = A2 * T2
eb = B2 * T2
fa = sa + ea
fb = sb + eb

if fa < fb:
  if sa < sb:
    print(0)
  elif sa == sb:
    print(1)
  elif sa > sb:
    d1 = sa - sb
    di = fb - fa
    c = int(d1 / di) + math.ceil(d1 / di)#  + 1
    print(c)
elif fa == fb:
  print("infinity")
elif fa > fb:
  if sa < sb:
    d1 = sb - sa
    di = fa - fb
    c = int(d1 / di) + math.ceil(d1 / di)# + 1
    print(c)
  elif sa == sb:
    print(1)
  elif sa > sb:
    print(0)