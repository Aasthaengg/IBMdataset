# Belongs to : midandfeed aka asilentvoice
import string
s = ""
while(1):
	try:
		s += str(input()).lower()
	except:
		break
		
alphabet = string.ascii_lowercase
ans = [0]*26
for x in s:	
	if x in alphabet:
		ans[ ord(x)-ord('a') ] += 1

for i in range(len(ans)):
	print("{} : {}".format(chr(i+ord('a')), ans[i]))