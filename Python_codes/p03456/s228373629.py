# ABC_086_B_1_21.py

a,b=list(map(int, input().split()))
ab=str(a)+str(b)
ab=int(ab)
flag=False
for i in range (320):
	if i**2==ab:
		flag=True
		break
if flag==True:
	print('Yes')
else:
	print('No')