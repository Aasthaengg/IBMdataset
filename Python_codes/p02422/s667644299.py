# 21-String-Transformation.py

# ???????????????
# ????????? str ?????????????????????????????????????????????????????????????????°????????????????????????????????????
# ???????????\?????????????????????????????§??????

# print a b: str ??? a ??????????????? b ??????????????§??????????????????
# reverse a b: str ??? a ??????????????? b ??????????????§?????????????????????
# replace a b p: str ??? a ??????????????? b ??????????????§??? p ?????????????????????
# ????????§??????????????? str ????????????????????? 0 ???????????¨????????????

# Input
# 1 ?????????????????? str ????????????????????????str ?????±?°????????????????????????????
# 2 ????????????????????° q ?????????????????????????¶???? q ??????????????????????¨??????¢?????§?????????????????????

# Output
# ??? print ???????????¨???????????????????????????????????????????????????

# Constraints
# 1???str????????????1000
# 1???q???100
# 0???a???b<str?????????
# replace ????????§??? b???a+1=p?????????

# Sample Input 1
# abcde
# 3
# replace 1 3 xyz
# reverse 0 2
# print 1 4
# Sample Output 1
# xaze

# Sample Input 2
# xyz
# 3
# print 0 2
# replace 0 2 abc
# print 0 2
# Sample Output 2
# xyz
# abc

#??\???

str = input()
op_num = int( input() )
for i in range(op_num):
	op = input().split()
	a = int(op[1])
	b = int(op[2])
	if op[0]=="replace":
		# str = str.replace(str[ a:b+1 ], op[3])
		str = str[0:a] + op[3] + str[b+1:]
	elif op[0]=="reverse":
		# str = str.replace(str[a:b+1], str[ b-len(str) : a-len(str)-1 : -1 ] )
		str = str[:a] + str[a:b+1][::-1] + str[b+1:]
	# elif op[0]=="print":
	else:
		print(str[a:b+1])