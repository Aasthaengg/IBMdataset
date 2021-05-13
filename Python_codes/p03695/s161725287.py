n = int(input())
et=0
arr = list(map(int , input().split()))
count = [0 for i in range(0,10)]
for i in range(0 , n):
	if arr[i]>=1 and arr[i]<=399:
		count[0]=count[0]+1
	elif arr[i]>=400 and arr[i]<=799:
		count[1]=count[1]+1
	elif arr[i]>=800 and arr[i]<=1199:
		count[2]=count[2]+1
	elif arr[i]>=1200 and arr[i]<=1599:
		count[3]=count[3]+1
	elif arr[i]>=1600 and arr[i]<=1999:
		count[4]=count[4]+1
	elif arr[i]>=2000 and arr[i]<=2399:
		count[5]=count[5]+1
	elif arr[i]>=2400 and arr[i]<=2799:
		count[6]=count[6]+1
	elif arr[i]>=2800 and arr[i]<=3199:
		count[7]=count[7]+1
	else:
		et = et+1
mn =1000
mx =0
tot=0
for i in range(0, 8):
	if count[i]>0:
		tot=tot+1
if tot==0:
	print(1,et)
else:
	print(tot , tot+et)
