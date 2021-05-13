n = int(input())
s = 100
a = 0
while n > s:
  s= int(s+s//100)
  a += 1
print(a)