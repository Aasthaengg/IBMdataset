x = sorted(input().split(), reverse=True)
a = (int(x[0])-int(x[1])) + (int(x[1])-int(x[2]))
if a < 0:
  a = a*-1
print(a)