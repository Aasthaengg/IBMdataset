x = int(input())
c = x // 11
c *= 2
r = x % 11
if(r > 6):
  c += 2
elif(r > 0):
  c += 1
print(c)
