from math import floor

X=int(input())

i = 1
money = 100
while 1:
  money = money + int(str(money)[:-2])
  if money>=X:
    break
  i+=1

print(i)
