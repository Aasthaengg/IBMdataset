A, B = map(int, input().split())
if A < 6:
  price = 0
elif A < 13:
  price =int(B/2)
else:
  price = B
print(price)