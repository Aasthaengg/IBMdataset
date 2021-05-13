s = str(input())
cnt_flag = False

for s_find in s:
	if s.count(s_find)>1:
		cnt_flag = True

if cnt_flag:
	print("no")

else:
	print("yes")
