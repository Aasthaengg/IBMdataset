x = int(input())
yokin = 100
i = 0
while True:
  yokin = yokin*101//100
  i = i + 1
  if (yokin >= x):
    break
print(i)