a,b = map(int, input().split())
sum = 0
if a == 1:
  sum = sum + 300000
elif a == 2:
  sum = sum + 200000
elif a == 3:
  sum = sum + 100000

if b == 1:
  sum = sum + 300000
elif b == 2:
  sum = sum + 200000
elif b == 3:
  sum = sum + 100000

if a == 1 and b == 1:
  sum = sum + 400000

print(sum)