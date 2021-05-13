a = input()
alp =[0 for i in range(0 , 29)]
for i in a:
	alp[ord(i)-ord('a')]+=1
for i in range(0 , 26):
	if alp[i]>1:
		print("no")
		exit()
print("yes")
exit()