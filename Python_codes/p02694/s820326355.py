import math
X =int(input())

deposit = 100
year = 0
while deposit<X:
  deposit = deposit+deposit//100
  #print(deposit)
  year+=1
  
print (year)