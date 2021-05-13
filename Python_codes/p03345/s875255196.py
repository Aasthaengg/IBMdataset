A, B, C, K = map(int, input().split())

o = B - A
e = A - B
if K % 2 == 0:
  r = e
else:
  r = o 
print(r)