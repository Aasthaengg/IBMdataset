x = int(input())

s = x // 11
a = x % 11
#print(s, a)
if 1 <= a <=6:
  print(2*s + 1)
elif 7 <= a < 11:
  print(2*s + 2)
elif a == 0:
  print(2*s)