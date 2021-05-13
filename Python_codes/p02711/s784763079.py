a = int(input())
toprint = False
while a > 0 :
 last_digit = a % 10
 a = a // 10
 if last_digit == 7 :
   toprint = True
 
if toprint == True :
 print ("Yes")
else :
 print ("No")