x = input()
x = int(x)
y1 = x // 11 * 2
p = x % 11
y2 = 0
if p > 0:
  y2 = 1
if p > 6:
  y2 = 2
# print("y1,y2,y=",y1,y2,y1+y2)
print(y1+y2)