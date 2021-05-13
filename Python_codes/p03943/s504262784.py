a=input().split(" ")
sum1=int(a[0])+int(a[1])
sum2=int(a[0])+int(a[2])
sum3=int(a[1])+int(a[2])

if sum1==int(a[2]) or sum2==int(a[1]) or sum3==int(a[0]):
	print("Yes")
else:
	print("No")