num = list(map(int, input().split()))
if(abs(num[0]-num[2])<=num[3] or (abs(num[0]-num[1])<=num[3] and abs(num[1]-num[2])<=num[3])):
	print("Yes")
else:
	print("No")