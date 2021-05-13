import sys

count = 0
num = []
while True:
	x = int(input())
	if x == 0 :
		break
	num.append(x)

for i in range(len(num)):
	print ("Case " + str((i+1)) + ":",num[i] )