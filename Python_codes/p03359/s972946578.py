a,b=(int(x) for x in input().split())
if a <= b:
  count = a
else:
  count = a - 1
print(count)