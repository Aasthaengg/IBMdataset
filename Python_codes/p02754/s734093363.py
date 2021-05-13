n,blue,red = [int(x) for x in input().split()]
p = n // (blue + red)
r = n % (blue + red)
if r > blue:
  c = blue
else:
  c = r
print(p * blue + c)