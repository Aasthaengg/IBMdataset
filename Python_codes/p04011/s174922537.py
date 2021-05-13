hotel=int(input())
hotel2=int(input())
hotel3=int(input())
hotel4=int(input())

if hotel > hotel2:
	sum1=int(hotel2)*int(hotel3)
	hotel5=int(hotel)-int(hotel2)
	sum2=int(hotel5)*int(hotel4)
	fee=int(sum1)+int(sum2)
else:
  fee=int(hotel)*int(hotel3)
 
print(str(fee))