#--Infinite Coins
cost = int(input())
one_coins = int(input())

for i in range(one_coins+1):
  calculate = cost - i
  if (calculate % 500 == 0):
    print ("Yes")
    exit()
  else:
    pass

print("No")
