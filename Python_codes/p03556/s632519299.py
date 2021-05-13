n=int(input())
for i in reversed(range(n+1)):
  if (i**.5).is_integer():
    print(i)
    break
