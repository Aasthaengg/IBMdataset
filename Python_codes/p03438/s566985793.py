n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

biggerA = 0
biggerB = 0
for ai, bi in zip(a, b):
  if ai > bi:
    biggerA += ai - bi
  if ai < bi:
    biggerB += (bi - ai) // 2
if biggerB >= biggerA:
  print("Yes")
else:
  print("No")
