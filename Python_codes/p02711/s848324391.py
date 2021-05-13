n=int(input().strip())
ans= False
while(n != 0):
	rem= n % 10
	if(rem == 7):
		ans= True
		break
	n = n // 10
if(ans):
	print("Yes")
else:
	print("No")