s_list = input()
for i in range(0 ,len(s_list)):
	if s_list[i] in s_list[i+1:]:
		print("no")
		exit(0)
print("yes")