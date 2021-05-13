W, a, b = map(int, input().split())
result = 0
if ((a <= b) and (b <= a + W)) or ((a <= b + W) and (b + W <= a + W)):
  result = 0
elif (b + W < a):
  result = a - (b + W)
elif (a + W < b):
  result = b - (a + W)
print(result)
