list_str2 = [0 for i in range(26)]

while(1):
	try:
		list_str1 = list(input())
		#print(list_str1)
	except:
		break
	for i in range(len(list_str1)):
		if 97 <= ord(list_str1[i].lower()) <= 122:
			list_str2[ord(list_str1[i].lower())-97] += 1

for i in range(26):
	print(chr(97+i)+' : '+str(list_str2[i]))