# 06-Repetitive_Processing-Print_Test_Cases.py

# ???????????±???????????????
# ????????????????????£????????§?????????????????????????????°??????????????°?????\??????????????????????????????????????£????????????????????£???????????????????????????????????????
# ???????????\????????????????????????????????°???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????´???????????§??????

# ???????????´??° x ???????????????????????????????????????????????????????????°?????????????????????????????????
# ?????????????????????????????\?????????????????????????????????????????????????????????????????????????????¨?????¨?????????????????????

# Input
# ??\???????????°????????????????????????????§????????????????????????????????????????????????????????????´??° x ??????????????????????§?????????????????????????
# x ??? 0 ?????¨?????\?????????????????????????????????????????????????????????????????????????????£????????????????????????
# Output
# ??????????????????????????¨????????\????????¢?????§ x ???????????????????????????

# Case i: x
# ????????§???i ?????????????§????????????????????????????????????????????????????Case??¨?????? i?????????????????????????????\??????????????????
# ?????????:?????????????????¨??´??° x ?????????????????????????????\????????????????????????????????\????????????????????????????????????

# Sample Input
# 3
# 5
# 11
# 7
# 8
# 19
# 0
# Sample Output
# Case 1: 3
# Case 2: 5
# Case 3: 11
# Case 4: 7
# Case 5: 8
# Case 6: 19

data=[]
i=0

# print("Input.")
while 1:
	data.append(int(input()))
	if data[i]==0:
		break;
	i=i+1

j=i

for i in range(j):
	print("Case {0}: {1}".format(i+1, data[i]))