# 12-Structured_Program_II-How_many_ways.py

# ????????????????????°
# 1 ?????? n ?????§?????°?????????????????????????????§???????????°?????????????????????????¨???? x ??¨??????
# ????????????????????°????±???????????????°?????????????????????????????????
# ????????°???1 ?????? 5 ?????§?????°???????????????????????§????????????????¨???? 9 ??¨???????????????????????????

# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# ??????????????????????????????

# Input
# ?????°??????????????????????????\?????¨???????????????????????????
# ???????????????????????§??????????????§??????????????? n???x ??? 1 ???????????????????????????

# n???x ?????¨?????? 0 ?????¨?????\?????????????????¨????????????
# n ??? 3 ??\??? 100?????\?????¨????????????

# Output
# ????????????????????????????????????????????????????????°????????????????????????????????????

# Sample Input
# 5 9
# 0 0
# Sample Output
# 2

result = []
n=[]
x=[]

while 1:
	temp = input().split() 
	if temp[0]=="0" and temp[1]=="0":
		break;
	else:
		n.append( int( temp[0] ))
		x.append( int( temp[1] ))

for i in range( len(n) ):
	count =0
	for n1 in range(1,n[i]+1-2):
		for n2 in range(n1+1, n[i]+1-1):
			for n3 in range(n2+1, n[i]+1):
				sum = n1+n2+n3
				if sum == x[i]:
					count+=1
	result.append(count)

for i in range( len(result) ):
	print(result[i])
	# if i == len(result)-1:
	# 	print(result[i])
	# else:
	# 	print("{0} ".format(result[i]), end="")