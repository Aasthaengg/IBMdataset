A, B = map(int, input().split())
if A + B >= 10:
  r = 'error'
else:
  r = int(A + B)
print(r)