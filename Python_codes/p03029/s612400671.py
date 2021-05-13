def LI():
  return [int(s) for s in input().split()]

A,P = LI()

print((A*3 + P) // 2)