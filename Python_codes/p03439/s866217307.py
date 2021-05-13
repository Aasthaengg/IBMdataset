n=int(input())
l=0
r=n
print(0)
l_color=input()[0]
for i in range(19):
	ans=(r-l)//2+l
	print(ans)
	x=input()[0]
	if x=="V":
		exit()
	elif (x==l_color and (ans-l)%2==1) or (x!=l_color and (ans-l)%2==0):
		r=ans
	else:
		l=ans
		l_color=x