n = int(input())
taro=0
hanako=0
for i in range(n):
	A=list(map(str,input().split()))
	if A[0]==A[1]:
		taro +=1
		hanako +=1
	else:
		B=sorted(A)#A???????????????????????????
		if A == B:#hanako??????????°???????
			hanako+=3
		else:
			taro+=3
print(taro,hanako)