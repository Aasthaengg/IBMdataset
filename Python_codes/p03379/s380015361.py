import copy
n = int(input())
x = list(map(int,input().split()))
x2 = copy.copy(x)
x2.sort()
num1,num2 = (len(x)//2)-1,(len(x)//2)
med1,med2 = x2[num1],x2[num2]
for i in range(n):
	if x[i] <= med1:
		print(med2)
	else:
		print(med1)