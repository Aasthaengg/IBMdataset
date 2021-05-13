num = int(input())
shutu = 0
if 400 <= num <= 599:
  shutu = 8
elif 600 <= num <= 799:
  shutu = 7
elif 800 <= num <= 999:
  shutu = 6 
elif 1000 <= num <= 1199:
  shutu = 5  
elif 1200 <= num <= 1399:
  shutu = 4
elif 1400 <= num <= 1599:
  shutu = 3 
elif 1600 <= num <= 1799:
  shutu = 2 
elif 1800 <= num <= 1999:
  shutu = 1
else:
  shutu = 0
print (shutu)