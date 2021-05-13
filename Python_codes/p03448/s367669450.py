#Coins
a = int(input()) #500円玉
b = int(input()) #100円玉
c = int(input()) #50円玉
x = int(input()) #総額
#硬貨の選び方は何通りあるか
count = 0
for i in range(0,a+1):
  y = x - 500 * i
  if y < 0:
    break
  for j in range(0,b+1):
    z = y - 100 * j
    if z < 0:
      break
    elif (z / 50) <= c:
      count += 1
print(count)